# Microsoft Speaker Recognition API: Python Sample
This repo contains Python samples (using Python 3) to demonstrate the use of Microsoft Speaker Recognition API.
* [Learn about the Speaker Recognition API](https://www.microsoft.com/cognitive-services/en-us/speaker-recognition-api)
* [Read the documentation](https://www.microsoft.com/cognitive-services/en-us/speaker-recognition-api/documentation)
* [Find more SDKs & Samples](https://www.microsoft.com/cognitive-services/en-us/SDK-Sample?api=speaker%20recognition)

## Run the Sample
First, you must obtain a free Speaker Recognition API subscription key here : (<https://www.microsoft.com/cognitive-services/en-us/sign-up>).

To use this sample application, there are four different scenarios:
 1. Create a user profile: `python Identification\CreateProfile.py <subscription_key>`
 2. Print all user profiles: `python Identification\PrintAllProfiles.py <subscription_key>`
 3. Enroll user profiles: `python Identification\EnrollProfile.py <subscription_key> <profile_id> <enrollment_file_path>`
 4. Identify test files: `python Identification\IdentifyFile.py <subscription_key> <identification_file_path> <profile_ids>...`

