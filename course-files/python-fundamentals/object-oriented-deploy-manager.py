class Deployment:
    """
    Manages the state and version history of a software deployment.
    """

    def __init__(self, service_name: str, environment: str):
        self.service_name: str = service_name
        self.environment: str = environment
        self.status = "pending"
        self.version = None
        self.old_version = []
        pass

    def deploy(self, new_version: str):
        self.status = "deployed"
        self.old_version.append(self.version)
        self.version = new_version
        pass

    def rollback(self) -> bool:
        if len(self.old_version) < 2:
            return False

        self.version = self.old_version.pop()
        self.status = "rolled_back"
        return True

    def check_status(self) -> dict:
        return {
            "service_name": self.service_name,
            "environment": self.environment,
            "status": self.status,
            "version": self.version,
        }
