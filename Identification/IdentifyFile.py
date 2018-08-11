import IdentificationServiceHttpClientHelper
import sys

def identify_file(subscription_key, file_path, force_short_audio, profile_ids):
    """Identify an audio file on the server.

    Arguments:
    subscription_key -- the subscription key string
    file_path -- the audio file path for identification
    profile_ids -- an array of test profile IDs strings
    force_short_audio -- waive the recommended minimum audio limit needed for enrollment
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        subscription_key)

    identification_response = helper.identify_file(
        file_path, profile_ids,
        force_short_audio.lower() == "true")

    print('Identified Speaker = {0}'.format(identification_response.get_identified_profile_id()))
    print('Confidence = {0}'.format(identification_response.get_confidence()))

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print('Usage: python IdentifyFile.py <subscription_key> <identification_file_path>'
              ' <profile_ids>...')
        print('\t<subscription_key> is the subscription key for the service')
        print('\t<identification_file_path> is the audio file path for identification')
        print('\t<force_short_audio> True/False waives the recommended minimum audio limit needed '
              'for enrollment')
        print('\t<profile_ids> the profile IDs for the profiles to identify the audio from.')
        sys.exit('Error: Incorrect Usage.')

    identify_file(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
