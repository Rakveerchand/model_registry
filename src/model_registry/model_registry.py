import boto3


def model_registry(sagemaker_role, model_package_group_name, model_url, batch_transform_image,
                   model_approval_status,
                   model_package_description):
    client = boto3.client('sagemaker')

    modelpackage_inference_specification = {
        "InferenceSpecification": {
            "Containers": [
                {
                    "Image": batch_transform_image,
                    "ModelDataUrl": model_url
                }
            ],
            "SupportedContentTypes": ["text/csv"],
            "SupportedResponseMIMETypes": ["text/csv"],
        }
    }

    model_package_group_name = model_package_group_name

    create_model_package_input_dict = {
        "ModelPackageGroupName": model_package_group_name,
        "ModelPackageDescription": model_package_description,
        "ModelApprovalStatus": model_approval_status
    }
    create_model_package_input_dict.update(modelpackage_inference_specification)

    create_model_package_response = client.create_model_package(**create_model_package_input_dict)
    model_package_arn = create_model_package_response["ModelPackageArn"]
    print('ModelPackage Version ARN : {}'.format(model_package_arn))

    models_list = client.list_model_packages(ModelPackageGroupName=model_package_group_name)
    print(models_list['ModelPackageSummaryList'][0]['ModelPackageVersion'])

    latest_model_version = models_list['ModelPackageSummaryList'][0]['ModelPackageVersion']
    model_name = f"{model_package_group_name}{latest_model_version}"

    container_list = [{'ModelPackageName': model_package_arn}]

    create_model_response = client.create_model(
        ModelName=model_name,
        ExecutionRoleArn=sagemaker_role,
        Containers=container_list
    )
    print("Model arn : {}".format(create_model_response["ModelArn"]))



