from dotenv import load_dotenv
import boto3
import os

# 1. Cargar variables del archivo .env
load_dotenv()

# 2. Crear sesión con AWS
session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

# 3. Crear cliente EC2
ec2_client = session.client("ec2")

# 4. Obtener todas las instancias
response = ec2_client.describe_instances()

# 5. Recorrer instancias y mostrar detalles
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance.get("InstanceId")
        state = instance.get("State", {}).get("Name")
        os_type = instance.get("PlatformDetails", "Unknown")

        print(f"Instance: {instance_id}  | State: {state}  | OS: {os_type}")
