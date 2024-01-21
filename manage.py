import sys
import subprocess

from api import app
from api.database import postgres_controler

class Runner:
    """API Started Class.
    """    
    @classmethod
    def main(self) ->None:
        """Main Function. API Started.
        """        
        if sys.argv[1] == "run":
            postgres_controler.create_security_table()
            subprocess.run(["uvicorn", "manage:app", "--port", "5050", "--host", "0.0.0.0"])

if __name__== "__main__":
    Runner.main()