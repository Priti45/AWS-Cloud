import boto3
from dotenv import load_dotenv
import os
load_dotenv()

def text_to_speech(text, output_file="output.mp3", voice_id="Joanna"):
    # AWS credentials and region
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_region = 'us-east-1'


    # Create Polly client
    polly_client = boto3.client('polly', region_name=aws_region, aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key)

    # Synthesize speech
    response = polly_client.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId=voice_id)

    # Save audio file
    with open(output_file, 'wb') as file:
        file.write(response['AudioStream'].read())

    print(f"Speech saved to {output_file}")

# Example usage
text_to_speech("Hello, this is a text-to-speech example using AWS Polly. Text-to-speech (TTS) is a type of assistive technology that reads digital text aloud. It's sometimes called “read aloud” technology. thank you!")

