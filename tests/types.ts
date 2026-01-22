// types.ts
export enum TerraformBackendConfig {
  AWS_ACCESS_KEY_ID = 'aws_access_key_id',
  AWS_SECRET_ACCESS_KEY = 'aws_secret_access_key',
  AWS_S3_BUCKET = 'aws_s3_bucket',
  AWS_S3_REGION = 'aws_s3_region',
  AWS_S3_KEY = 'aws_s3_key',
}

export interface TerraformBackendConfigObject {
  [key in TerraformBackendConfig]: string;
}

export type TerraformConfig = {
  backend: {
    type: string;
    config: TerraformBackendConfigObject;
  };
  required_providers: {
    [key: string]: {
      source: string;
      version: string;
    };
  };
};