def generate_rdp_file() -> None:
    stack_outputs = get_stack_outputs(stack_name=get_stack_name(BASE_NAME))
    ec2_client: EC2Client = boto3.client('ec2', region_name=os.environ['REGION'])
    response = ec2_client.get_password_data(InstanceId=stack_outputs["EC2ID"])
    ec2_password = decrypt_password_data(response)

    with open('client_ec2_connection.rdp', 'w', encoding='utf-8') as f:
        f.write(f'full address:s:{stack_outputs.get("EC2IP","")}\n')
        f.write(f'server port:i:{stack_outputs.get("EC2PORT","3389")}\n')
        f.write(f'username:s:{stack_outputs.get("EC2USERNAME","Administrator")}\n')
        f.write('prompt for credentials:i:1\n')
    print('Copy below password, open the client_ec2_connection.rdp to connect to machine, enter copied password when prompted.')
    print(f'PASSWORD: {ec2_password}')


def decrypt_password_data(password_data):
    encrypted_password = password_data['PasswordData']

    with open('client_ec2_key.pem', encoding='utf-8') as pk_file:
        pk_contents = pk_file.read()

    private_key = rsa.PrivateKey.load_pkcs1(pk_contents.encode('latin-1'))
    value = base64.b64decode(encrypted_password)
    value = rsa.decrypt(value, private_key)
    decrypted_password = value.decode('utf-8')

    return decrypted_password
