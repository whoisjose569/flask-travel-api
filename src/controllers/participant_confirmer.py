from typing import Dict

class ParticipantsConfirmer:
    def __init__(self, participants_repository) -> None:
        self.__participants_repository = participants_repository
    
    def confirm(self, participant_id) -> Dict:
        try:
            self.__participants_repository.update_participant_status(participant_id)
            return {"body": None, "status_code": 204}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }