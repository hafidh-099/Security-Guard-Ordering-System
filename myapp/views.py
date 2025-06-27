from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Organization, SecurityOffice, Order, ArmedSecurityGuard
from .serializers import OrganizationSerializer, SecurityOfficeSerializer, OrderSerializer, ArmedSecurityGuardSerializer


# ------------------- Generic CRUD View -------------------
def generic_api(model_class, class_serializer):
    @api_view(['GET', 'POST', 'PUT', 'DELETE'])
    @permission_classes([IsAuthenticated])
    def api(request, pk=None):

        # ------------------- GET -------------------
        if request.method == 'GET':
            if pk:
                try:
                    instance = model_class.objects.get(pk=pk)
                    serializer = class_serializer(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'Message': 'Object not found'}, status=404)
            else:
                instances = model_class.objects.all()

                # Filter Orders for Organization or Security Office
                if model_class == Order:
                    try:
                        org = Organization.objects.get(user=request.user)
                        instances = model_class.objects.filter(Organization_name=org)
                    except Organization.DoesNotExist:
                        try:
                            office = SecurityOffice.objects.get(user=request.user)
                            instances = model_class.objects.filter(Office_name=office)
                        except SecurityOffice.DoesNotExist:
                            instances = model_class.objects.none()

                # Filter Guards to only those created by the logged-in security office
                if model_class == ArmedSecurityGuard:
                    try:
                        office = SecurityOffice.objects.get(user=request.user)
                        instances = model_class.objects.filter(worked_office=office)
                    except SecurityOffice.DoesNotExist:
                        instances = model_class.objects.none()

                serializer = class_serializer(instances, many=True)
                return Response(serializer.data)

        # ------------------- POST -------------------
        elif request.method == 'POST':
            data = request.data.copy()

            # Attach logged-in Organization to Order
            if model_class == Order:
                try:
                    org = Organization.objects.get(user=request.user)
                    data['Organization_name'] = org.id
                except Organization.DoesNotExist:
                    return Response({'error': 'Organization not found for this user'}, status=400)

            # Attach logged-in Security Office to Guard
            if model_class == ArmedSecurityGuard:
                try:
                    office = SecurityOffice.objects.get(user=request.user)
                    data['worked_office'] = office.id
                except SecurityOffice.DoesNotExist:
                    return Response({'error': 'Security Office not found for this user'}, status=400)

            serializer = class_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                print("Serializer errors:", serializer.errors)
                return Response(serializer.errors, status=400)

        # ------------------- PUT -------------------
        elif request.method == 'PUT':
            if pk:
                try:
                    instance = model_class.objects.get(pk=pk)
                    serializer = class_serializer(instance, data=request.data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    return Response(serializer.errors, status=400)
                except model_class.DoesNotExist:
                    return Response({'Message': 'Object not found'}, status=404)

        # ------------------- DELETE -------------------
        elif request.method == 'DELETE':
            if pk:
                try:
                    instance = model_class.objects.get(pk=pk)
                    instance.delete()
                    return Response({'Message': 'Object deleted successfully'}, status=204)
                except model_class.DoesNotExist:
                    return Response({'Message': 'Object not found'}, status=404)

        return Response({'Message': 'Invalid request'}, status=400)

    return api


# ------------------- API Endpoints -------------------
manage_order = generic_api(Order, OrderSerializer)
manage_SecurityOffice = generic_api(SecurityOffice, SecurityOfficeSerializer)
manage_ArmedSecurityGuard = generic_api(ArmedSecurityGuard, ArmedSecurityGuardSerializer)
manage_Organization = generic_api(Organization, OrganizationSerializer)


# ------------------- Login Views -------------------
@api_view(['POST'])
@permission_classes([])  # Public access, no auth required
def login_organization(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Username and password required'}, status=400)

    user = authenticate(username=username, password=password)
    if user:
        try:
            org = Organization.objects.get(user=user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'role': 'organization'})
        except Organization.DoesNotExist:
            return Response({'error': 'User is not an organization'}, status=403)
    return Response({'error': 'Invalid credentials'}, status=401)


@api_view(['POST'])
@permission_classes([])  # Public access, no auth required
def login_securityoffice(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Username and password required'}, status=400)

    user = authenticate(username=username, password=password)
    if user:
        try:
            office = SecurityOffice.objects.get(user=user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'role': 'security_office',
                'securityoffice_id': office.id  # <-- Added this for frontend filtering
            })
        except SecurityOffice.DoesNotExist:
            return Response({'error': 'User is not a security office'}, status=403)
    return Response({'error': 'Invalid credentials'}, status=401)


# ------------------- Register Views -------------------
@api_view(['POST'])
@permission_classes([])  # Public access, no auth required
def register_organization(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    location = data.get('location')
    bussiness = data.get('bussiness')
    status_field = data.get('status')

    if not all([username, password, name, location, bussiness, status_field]):
        return Response({'error': 'Missing required fields'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create(username=username, password=make_password(password))
    Organization.objects.create(
        user=user,
        name=name,
        location=location,
        bussiness=bussiness,
        status=status_field
    )
    return Response({'message': 'Organization registered successfully'}, status=201)


@api_view(['POST'])
@permission_classes([])  # Public access, no auth required
def register_securityoffice(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    officename = data.get('officename')
    location = data.get('location')
    status_field = data.get('status')

    if not all([username, password, officename, location, status_field]):
        return Response({'error': 'Missing required fields'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create(username=username, password=make_password(password))
    SecurityOffice.objects.create(
        user=user,
        officename=officename,
        location=location,
        status=status_field
    )
    return Response({'message': 'Security office registered successfully'}, status=201)
