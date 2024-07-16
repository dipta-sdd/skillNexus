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


@ swagger_auto_schema(
    methods=['get'],
    operation_summary="Get Employer Company",
    security=[{"Bearer": []}]
)
@ api_view(['GET'])
def getCompany(req):
    user = getUser(req)
    print('___________________________________________________________________________________________')
    try:
        obj = Company.objects.get(user=user['id'])
        company = CompanySerializer(obj)
        print(company.data)
        return Response(company.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'No company details found.'}, status=status.HTTP_204_NO_CONTENT)


@ swagger_auto_schema(
    methods=['post'],
    operation_summary="Add employer company ",
    request_body=ExperienceSeriallizer,
    security=[{"Bearer": []}]
)
@ api_view(['POST'])
def addCompany(req):
    user = getUser(req)
    data = req.data.copy()
    data['user'] = user['id']
    try:
        obj = Company.objects.get(user=user['id'])
        company = CompanySerializer(obj, data=data, partial=True)
    except:
        company = CompanySerializer(data=data)
    if company.is_valid():
        company.save()
        return Response(company.data, status=status.HTTP_201_CREATED)
    return Response(company.errors, status=status.HTTP_400_BAD_REQUEST)


@ swagger_auto_schema(
    methods=['get'],
    operation_summary="Get University",
    security=[{"Bearer": []}]
)
@ api_view(['GET'])
def getUniversity(req):
    user = getUser(req)
    print('___________________________________________________________________________________________')
    try:
        obj = University.objects.get(user=user['id'])
        university = UniversitySerializer(obj)
        print(university.data)
        return Response(university.data, status=status.HTTP_200_OK)
    except:
        return Response({'message': 'No university details found.'}, status=status.HTTP_204_NO_CONTENT)


@ swagger_auto_schema(
    methods=['post'],
    operation_summary="Add university ",
    request_body=UniversitySerializer,
    security=[{"Bearer": []}]
)
@ api_view(['POST'])
def addUniversity(req):
    user = getUser(req)
    data = req.data.copy()
    data['user'] = user['id']
    try:
        obj = University.objects.get(user=user['id'])
        university = UniversitySerializer(obj, data=data, partial=True)
    except:
        university = UniversitySerializer(data=data)
    if university.is_valid():
        university.save()
        return Response(university.data, status=status.HTTP_201_CREATED)
    return Response(university.errors, status=status.HTTP_400_BAD_REQUEST)


@ swagger_auto_schema(
    methods=['post'],
    operation_summary="Add university program/course ",
    request_body=UniversityProgramSerial,
    security=[{"Bearer": []}]
)
@ api_view(['POST'])
def addProgram(req):
    user = getUser(req)
    data = req.data.copy()
    data['user'] = user['id']
    if 'id' in data:
        obj = UniversityProgram.objects.get(id=data['id'], user=user['id'])
        program = UniversityProgramSerial(obj, data=data, partial=True)
    else:
        program = UniversityProgramSerial(data=data)
    if program.is_valid():
        program.save()
        return Response(program.data, status=status.HTTP_201_CREATED)
    return Response(program.errors, status=status.HTTP_400_BAD_REQUEST)


@ swagger_auto_schema(
    methods=['get'],
    operation_summary="Get programs ans courses",
    security=[{"Bearer": []}]
)
@ api_view(['GET'])
def getProgram(req):
    user = getUser(req)
    try:
        if 'program_id' in req.query_params:
            objs = UniversityProgram.objects.filter(
                user=user['id'], id=req.query_params['program_id'])
        else:
            objs = UniversityProgram.objects.filter(user=user['id'])
        print(objs)
        program = UniversityProgramSerial(objs, many=True)
        return Response(program.data, status=status.HTTP_200_OK)
    except:
        return Response({'msg': 'No program or course Found'}, status=status.HTTP_204_NO_CONTENT)


@ swagger_auto_schema(
    methods=['delete'],
    operation_summary="Delete program or course",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['program_id'],
        properties={
            'program_id': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    security=[{"Bearer": []}]
)
@ api_view(['DELETE'])
def deelProgram(req):
    user = getUser(req)
    program_id = req.data['program_id']
    try:
        program = UniversityProgram.objects.get(id=program_id, user=user['id'])
        program.delete()
        return Response({"message": "Program has been deleted"}, status=status.HTTP_200_OK)
    except UniversityProgram.DoesNotExist:
        return Response({"error": "Program record not found or does not belong to the user"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ api_view(['POST'])
def addCourse(req):
    print('_____________________add training_______________________')
    user = getUser(req)
    data = req.data.copy()
    data['user'] = user['id']
    # if 'id' in data:
    #     obj = Experience.objects.get(id=data['id'], user=user['id'])
    #     serializer = ExperienceSeriallizer(obj, data=data, partial=True)
    # else:

    serializer = CourseSeriallizer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ api_view(['GET'])
def getCourseDetail(req):
    user = getUser(req)
    try:
        if 'course_id' in req.query_params:
            objs = Course.objects.filter(
                user=user['id'], id=req.query_params['course_id'])
        else:
            objs = Course.objects.filter(user=user['id'])
        print(objs)
        course = CourseSeriallizer(objs, many=True)
        return Response(course.data, status=status.HTTP_200_OK)
    except:
        return Response({'msg': 'No Course Found'}, status=status.HTTP_204_NO_CONTENT)


@ api_view(['DELETE'])
def delcourse(req):
    user = getUser(req)

    course_id = req.data['course_id']
    try:
        course = Course.objects.get(id=course_id, user=user['id'])
        course.delete()
        print(course)
        return Response({"message": "Course has been deleted"}, status=status.HTTP_200_OK)
    except Course.DoesNotExist:
        return Response({"error": "Course record not found or does not belong to the user"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ api_view(['POST'])
def addCourseLecture(req):
    print('_____________________add Lecture_______________________')
    user = getUser(req)
    #print(user)
    print(req.data)
    data = req.data.dict()
    data['user'] = user['id']
    print(data)
    serializer = CourseLectureSeriallizer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delCourse(request):
    user = request.user  # Assuming you're using Django Rest Framework's authentication
    # Use request.data.get to safely retrieve data
    course_id = request.data.get('course_id')

    try:
        course = Course.objects.get(id=course_id, user=user)
        course.delete()
        return Response({"message": "Course has been deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Course.DoesNotExist:
        return Response({"error": "Course record not found or does not belong to the user"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def editCourse(request):
    print('___________________________')
    user = request.user
    course_id = request.data.get('course_id')
    try:
        course = Course.objects.get(id=course_id, user=user)
        course.title = request.data.get('title', course.title)
        course.course_outcome = request.data.get(
            'course_outcome', course.course_outcome)
        course.course_contain = request.data.get(
            'course_contain', course.course_contain)

        if 'course_thumbnil' in request.FILES:
            course.course_thumbnil = request.FILES['course_thumbnil']

        course.save()
        return Response({"message": "Course has been updated"}, status=status.HTTP_200_OK)
    except Course.DoesNotExist:
        return Response({"error": "Course record not found or does not belong to the user"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ api_view(['GET'])
def getLectureDetail(req):
    user = getUser(req)
    try:
        if 'course_id' in req.query_params:
            objs = CourseLecture.objects.filter(
                user=user['id'], id=req.query_params['course_id'])
        else:
            objs = CourseLecture.objects.filter(user=user['id'])
        print(objs)
        course = CourseLectureSeriallizer(objs, many=True)
        return Response(course.data, status=status.HTTP_200_OK)
    except:
        return Response({'msg': 'No Lecture Found'}, status=status.HTTP_204_NO_CONTENT)


@ api_view(['GET'])
def getCourseVideo(req):
    user = getUser(req)
    try:
        if 'course_id' in req.query_params:
            objs = CourseLecture.objects.filter(
                user=user['id'], id=req.query_params['course_id'])
        else:
            objs = CourseLecture.objects.filter(user=user['id'])
        print(objs)
        course = CourseLectureSeriallizer(objs, many=True)
        return Response(course.data, status=status.HTTP_200_OK)
    except:
        return Response({'msg': 'No Lecture Found'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def edit_course_video(request):
    try:
        user = getUser(request)  # Assuming `getUser` retrieves user info
        course_id = request.query_params.get('course_id')

        if course_id:
            objs = CourseLecture.objects.filter(user=user['id'], id=course_id)
        else:
            objs = CourseLecture.objects.filter(user=user['id'])

        if objs.exists():
            serializer = CourseLectureSeriallizer(objs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No Lecture Found'}, status=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        return Response({'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@ api_view(['GET'])
def courselist(req):
    try:
        if 'course_id' in req.query_params:
            objs = Course.objects.filter(id=req.query_params['course_id'])
        else:
            objs = Course.objects.filter()
        print(objs)
        course = CourseSeriallizer(objs, many=True)
        return Response(course.data, status=status.HTTP_200_OK)
    except:
        return Response({'msg': 'No Course Found'}, status=status.HTTP_204_NO_CONTENT)


@ api_view(['GET'])
def getSingleCourseDetail(req):

    try:
        if 'course_id' in req.query_params:
            objs = Course.objects.filter(
                id=req.query_params['course_id'])
        else:
            objs = Course.objects.filter()
        print(objs)
        course = CourseSeriallizer(objs, many=True)
        return Response(course.data, status=status.HTTP_200_OK)
    except:
        return Response({'msg': 'No Course Found'}, status=status.HTTP_204_NO_CONTENT)





@api_view(['GET'])
def get_lectures(request):
    course_id = request.query_params.get('course_id')
    if not course_id:
        return Response({'error': 'Course ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        lectures = CourseLecture.objects.filter(course_id=course_id)
        serializer = CourseLectureSeriallizer(lectures, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except CourseLecture.DoesNotExist:
        return Response({'error': 'Lectures not found'}, status=status.HTTP_404_NOT_FOUND)
    



  
@ api_view(['GET'])
def getProgramStudent(req):
    with connection.cursor() as cursor:
        cursor.execute(
            f"select data_universityProgram.id,data_universityProgram.name, data_universityProgram.type , data_universityProgram.duration_year , data_universityProgram.duration_month , data_universityProgram.description , data_university.user_id, data_university.name , data_university.address from data_universityProgram , data_university where data_university.user_id = data_universityProgram.user_id")
        edus = cursor.fetchall()
        print(edus)
        edus = [dict(zip(['id', 'name', 'type', 'duration_year', 'duration_month', 'description',
                     'university_id', 'university_name', 'university_address'], edu)) for edu in edus]
        print(edus)
        return Response(edus, status=status.HTTP_200_OK)



@api_view(['GET'])

def get_course_list_single(request):
    course_id = request.GET.get('course_id')
    courses = Course.objects.filter(id=course_id)
    response_data = []
    
    for course in courses:
        course_data = CourseSeriallizer(course).data
        # Check if the user is already enrolled
        is_enrolled = Enrollment.objects.filter(course=course, user=request.user).exists()
        course_data['is_enrolled'] = is_enrolled
        response_data.append(course_data)

    return Response(response_data)




# @api_view(['POST'])
# def course_enroll(request):
#     try:
#          course_id = request.GET.get('course_id')
#     except Course.DoesNotExist:
#         return Response({'detail': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

#     # Get the user (assuming you have a way to retrieve the user from the request)
#     user = getUser(request)

#     # Check if the user is already enrolled in the course
#     if Enrollment.objects.filter(course=course_id, user=user).exists():
#         return Response({'detail': 'Already enrolled in this course.'}, status=status.HTTP_400_BAD_REQUEST)
    
#     # Enroll the user
#     enrollment = Enrollment.objects.create(course=course_id, user=user)
#     return Response({'detail': 'Successfully enrolled in the course.'}, status=status.HTTP_201_CREATED)



# @api_view(['GET'])
# def check_enrollment(request):
#     course_id = request.GET.get('course_id')
#     try:
#         course = Course.objects.get(id=course_id)
#     except Course.DoesNotExist:
#         return Response({'enrolled': False}, status=status.HTTP_404_NOT_FOUND)

#     user = getUser(request)

#     # Check if the user is enrolled in the course
#     is_enrolled = Enrollment.objects.filter(course=course, user=user).exists()

#     return Response({'enrolled': is_enrolled})



@api_view(['POST'])
def course_enroll(request):
    course_id = request.data.get('course_id')  # Use request.data to retrieve POST data
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({'detail': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user  # Assuming you have authentication middleware to get the user

    # Check if the user is already enrolled in the course
    if Enrollment.objects.filter(course=course, user=user).exists():
        return Response({'detail': 'Already enrolled in this course.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Enroll the user
    enrollment = Enrollment.objects.create(course=course, user=user)
    return Response({'detail': 'Enrolled successfully.'}, status=status.HTTP_200_OK)



@api_view(['GET'])
def check_enrollment(request):
    course_id = request.query_params.get('course_id')
    user = request.user

    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({'detail': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user is enrolled in the course
    is_enrolled = Enrollment.objects.filter(course=course, user=user).exists()
    return Response({'enrolled': is_enrolled}, status=status.HTTP_200_OK)

