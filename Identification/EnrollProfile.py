import IdentificationServiceHttpClientHelper
import sys

def enroll_profile(subscription_key, profile_id, file_path, force_short_audio):
    """Enrolls a profile on the server.

    Arguments:
    subscription_key -- the subscription key string
    profile_id -- the profile ID of the profile to enroll
    file_path -- the path of the file to use for enrollment
    force_short_audio -- waive the recommended minimum audio limit needed for enrollment
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        subscription_key)

    enrollment_response = helper.enroll_profile(
        profile_id,
        file_path,
        force_short_audio.lower() == "true")

    print('Total Enrollment Speech Time = {0}'.format(enrollment_response.get_total_speech_time()))
    print('Remaining Enrollment Time = {0}'.format(enrollment_response.get_remaining_speech_time()))
    print('Speech Time = {0}'.format(enrollment_response.get_speech_time()))
    print('Enrollment Status = {0}'.format(enrollment_response.get_enrollment_status()))

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print('Usage: python EnrollProfile.py <subscription_key> <profile_id> '
            '<enrollment_file_path>')
        print('\t<subscription_key> is the subscription key for the service')
        print('\t<profile_id> is the profile ID of the profile to enroll')
        print('\t<enrollment_file_path> is the enrollment audio file path')
        print('\t<force_short_audio> True/False waives the recommended minimum audio limit needed '
              'for enrollment')

        sys.exit('Error: Incorrect Usage.')

    enroll_profile(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
