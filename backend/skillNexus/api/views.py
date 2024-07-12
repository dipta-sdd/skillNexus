# views.py
from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from data.models import *
from data.serializers import *
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


def getUser(request):
    if isinstance(request.user, User):
        serializer = UserSerializer(request.user)
        return serializer.data


@swagger_auto_schema(
    methods=['get'],
    operation_summary="Get Current User",
    # request_body=editUserSerializer,
    security=[{"Bearer": []}]
)
@api_view(['GET'])
def current_user(request):
    if isinstance(request.user, User):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    else:
        return Response({"detail": "Authentication credentials were not provided."}, status=401)


@swagger_auto_schema(
    methods=['post'],
    operation_summary="Create User",
    # operation_description="Create a new user account.",
    request_body=UserSerializer,
    # request_body=openapi.Schema(
    #     type=openapi.TYPE_OBJECT,
    #     required=['username', 'email', 'password'],
    #     properties={
    #         'username': openapi.Schema(type=openapi.TYPE_STRING),
    #         'email': openapi.Schema(type=openapi.TYPE_STRING),
    #         'password': openapi.Schema(type=openapi.TYPE_STRING)
    #     }
    # ),
    # security=[{"Bearer": []}]
)
@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(
                serializer.validated_data.get('password'))
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['post'],
    operation_summary="Login",
    request_body=LoginSerializer,
    # security=[{"Bearer": []}]
)
@api_view(['POST'])
@permission_classes([])
def login_view(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            raw_password = serializer.validated_data['password']
            print('here')
            # Retrieve the user from the database using the provided username
            user = User.objects.get(username=username)
            # Check if the provided raw password matches the hashed password in the database
            if check_password(raw_password, user.password):
                login(request, user)

                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({"message": "Login successful", "access_token": access_token}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['post'],
    operation_summary="Edit Profile",
    request_body=editUserSerializer,
    security=[{"Bearer": []}]
)
@api_view(['POST'])
def editProfile(request):
    print("________________________edit_profile_______________________")
    user = request.user
    print(user)
    serializer = editUserSerializer(
        user, data=request.data, partial=True)  # For partial updates
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    methods=['Post'],
    operation_summary="Personal Details",
    request_body=PersonalDetailsSerializer
)
@api_view(['POST'])
def getPersonaDetails(req):
    print("____________________get_personal_details_____________________")
    data = req.data

    try:
        obj = PersonalDetails.objects.get(pk=data['id'])
        serializer = PersonalDetailsSerializer(obj)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except PersonalDetails.DoesNotExist:
        return Response({"error": "Personal details not found"}, status=status.HTTP_404_NOT_FOUND)


@ swagger_auto_schema(
    methods=['post'],
    operation_summary="Edit Personal Details",
    request_body=PersonalDetailsSerializer,
    security=[{"Bearer": []}]
)
@ api_view(['POST'])
def editPersonaDetails(request):
    print("________________________Edit Personal Details_______________________")
    try:
        instance = PersonalDetails.objects.get(
            id=request.data['id'])  # check if details already exists
        # if exists update it
        serializer = PersonalDetailsSerializer(instance=instance,
                                               data=request.data, partial=True)
    except:
        # if not exists create new
        serializer = PersonalDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['POST'])
def edu_level(req):
    user = getUser(req)
    # print(user)
    if req.method == 'GET':
        try:
            obj = Edu_level.objects.all()
            serializer = Edu_levelSerializer(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': 'No level Found'}, status=status.HTTP_204_NO_CONTENT)
    elif req.method == 'POST' and user['role'] == 'Admin':
        serializer = Edu_levelSerializer(data=req.data, partial=True)
        if serializer.is_valid():
            level = serializer.save()
            return Response(Edu_levelSerializer(level).data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(["GET", 'POST'])
def edu_degree(req):
    user = getUser(req)
    if req.method == 'GET':
        try:
            obj = Edu_degree.objects.get()
            serializer = Edu_degreeSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': 'No degree found'}, status=status.HTTP_204_NO_CONTENT)
    elif req.method == 'POST' and user['role'] == 'Admin':
        serializer = Edu_degreeSerializer(data=req.data, partial=True)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(["GET", 'POST'])
def edu_group_or_mejor(req):
    user = getUser(req)
    if req.method == 'GET':
        try:
            obj = Edu_group_or_major.objects.get()
            serializer = Edu_group_or_majorSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': 'No group/major Found'}, status=status.HTTP_204_NO_CONTENT)
    elif req.method == 'POST' and user['role'] == 'Admin':
        serializer = Edu_group_or_majorSerializer(data=req.data, partial=True)
        # print(req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(["GET", ])
def edu_get(req):
    with connection.cursor() as cursor:
        cursor.execute(
            "select * from data_edu_level")
        levels = cursor.fetchall()
        levels = [dict(zip(['name', 'id'], level))
                  for level in levels]
        # result= []
        for level in levels:
            # print(level['id'])
            cursor.execute(
                f"select name,id from data_edu_degree where level_id={level['id']}")
            degrees = cursor.fetchall()
            degrees = [dict(zip(['name', 'id'], degree)) for degree in degrees]
            for degree in degrees:
                cursor.execute(
                    f"select name,id from data_edu_group_or_major where degree_id={degree['id']}")
                groups = cursor.fetchall()
                groups = [dict(zip(['name', 'id'], group))
                          for group in groups]
                degree['groups'] = groups
            level['degrees'] = degrees
        return Response(levels, status=status.HTTP_200_OK)


@ swagger_auto_schema(
    methods=['post'],
    operation_summary="Edit Education (user)",
    request_body=EducationSerializer,
    security=[{"Bearer": []}]
)
@ api_view(['POST'])
def addEducation(req):
    user = getUser(req)
    data = req.data.copy()
    # print(user)
    # print(req.data)
    data['user'] = user['id']
    # print(data)
    if 'id' in data:
        obj = Education.objects.get(id=data['id'], user=user['id'])
        serializer = EducationSerializer(obj, data=data, partial=True)
    else:
        serializer = EducationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ swagger_auto_schema(
    methods=['get'],
    operation_summary="Get Education (user)",
    security=[{"Bearer": []}]
)
@ api_view(['GET'])
def getEducation(req):
    user = getUser(req)
    print('-------------------get education of a user------------------------')
    with connection.cursor() as cursor:
        cursor.execute(
            f"select data_education.id, data_edu_level.name, data_edu_degree.name, data_edu_group_or_major.name , result_type , result, gpa, gpa_scale,institute, passing_year from data_education, data_edu_level, data_edu_degree, data_edu_group_or_major where data_education.level_id=data_edu_level.id and data_education.degree_id=data_edu_degree.id and data_education.group_id=data_edu_group_or_major.id and user_id={user['id']}")
        edus = cursor.fetchall()
        # print(edus)
        edus = [dict(zip(['id', 'name', 'degree', 'group', 'result_type', 'result', 'gpa', 'gpa_scale', 'institute', 'passing_year'], edu))
                for edu in edus]
        print(edus)
        return Response(edus, status=status.HTTP_200_OK)


@ swagger_auto_schema(
    methods=['delete'],
    operation_summary="Delete Education (user)",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['education_id'],
        properties={
            'education_id': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    security=[{"Bearer": []}]
)
@ api_view(['DELETE'])
def delEducation(req):
    user = getUser(req)

    education_id = req.data['education_id']
    try:
        education = Education.objects.get(id=education_id, user=user['id'])
        education.delete()
        print(education)
        return Response({"message": "Education has been deleted"}, status=status.HTTP_200_OK)
    except Education.DoesNotExist:
        return Response({"error": "Education record not found or does not belong to the user"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ swagger_auto_schema(
    methods=['post'],
    operation_summary="Add Training ",
    request_body=TrainingSerializer,
    security=[{"Bearer": []}]
)
@ api_view(['POST'])
def addTraining(req):
    print('_____________________add training_______________________')
    user = getUser(req)
    data = req.data.copy()
    data['user'] = user['id']
    if 'id' in data:
        obj = Training.objects.get(id=data['id'], user=user['id'])
        serializer = TrainingSerializer(obj, data=data, partial=True)
    else:
        serializer = TrainingSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ swagger_auto_schema(
    methods=['delete'],
    operation_summary="Delete Training",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['training_id'],
        properties={
            'training_id': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    security=[{"Bearer": []}]
)
@ api_view(['DELETE'])
def delTraining(req):
    user = getUser(req)
    training_id = req.data['training_id']
    try:
        training = Training.objects.get(id=training_id, user=user['id'])
        training.delete()
        return Response({"message": "Training has been deleted"}, status=status.HTTP_200_OK)
    except Training.DoesNotExist:
        return Response({"error": "Training record not found or does not belong to the user"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ swagger_auto_schema(
    methods=['get'],
    operation_summary="Get Training",
    security=[{"Bearer": []}]
)
@ api_view(['GET'])
def getTraining(req):
    user = getUser(req)
    print('-------------------get training of a user------------------------')

    try:
        if 'training_id' in req.query_params:
            objs = Training.objects.filter(
                user=user['id'], id=req.query_params['training_id'])
        else:
            objs = Training.objects.filter(user=user['id'])
        print(objs)
        trainings = TrainingSerializer(objs, many=True)
        return Response(trainings.data, status=status.HTTP_200_OK)
    except:
        return Response({'msg': 'No Traings Found'}, status=status.HTTP_204_NO_CONTENT)

# experience


@ swagger_auto_schema(
    methods=['post'],
    operation_summary="Add Experience ",
    request_body=ExperienceSeriallizer,
    security=[{"Bearer": []}]
)
@ api_view(['POST'])
def addExperience(req):
    print('_____________________add training_______________________')
    user = getUser(req)
    data = req.data.copy()
    data['user'] = user['id']
    if 'id' in data:
        obj = Experience.objects.get(id=data['id'], user=user['id'])
        serializer = ExperienceSeriallizer(obj, data=data, partial=True)
    else:
        serializer = ExperienceSeriallizer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ swagger_auto_schema(
    methods=['delete'],
    operation_summary="Delete Training",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['experience_id'],
        properties={
            'experience_id': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    security=[{"Bearer": []}]
)
@ api_view(['DELETE'])
def delExperience(req):
    user = getUser(req)
    experience_id = req.data['experience_id']
    try:
        experience = Experience.objects.get(id=experience_id, user=user['id'])
        experience.delete()
        return Response({"message": "Experience has been deleted"}, status=status.HTTP_200_OK)
    except Experience.DoesNotExist:
        return Response({"error": "Experience record not found or does not belong to the user"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ swagger_auto_schema(
    methods=['get'],
    operation_summary="Get Experience",
    security=[{"Bearer": []}]
)
@ api_view(['GET'])
def getExperience(req):
    user = getUser(req)
    try:
        if 'experience_id' in req.query_params:
            objs = Experience.objects.filter(
                user=user['id'], id=req.query_params['experience_id'])
        else:
            objs = Experience.objects.filter(user=user['id'])
        print(objs)
        experiences = ExperienceSeriallizer(objs, many=True)
        return Response(experiences.data, status=status.HTTP_200_OK)
    except:
        return Response({'msg': 'No Experience Found'}, status=status.HTTP_204_NO_CONTENT)
