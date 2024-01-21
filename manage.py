import sys
import subprocess

from api import app

class Runner:
    @classmethod
    def main(self) ->None:
        """Main Function. API Started.
        """        
        if sys.argv[1] == "run":
            subprocess.run(["uvicorn", "manage:app", "--port", "5050", "--host", "0.0.0.0"])

if __name__== "__main__":
    Runner.main()