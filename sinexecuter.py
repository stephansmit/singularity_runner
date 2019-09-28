from spython.main import Client as client
import subprocess
import os
class SinExecuter(object):
    def __init__(self, img_name, img_url, img_dir):
        self.img_name = img_name
        self.img_url = img_url
        self.img_dir = img_dir

    def _make_dir(self):
        subprocess.check_call(['mkdir', '-p', self.img_dir])

    def _pull_image(self):
        client.pull(image=self.img_url,name=self.img_name, pull_folder=self.img_dir)
        return

    def run(self, cmd, bind_dir):
        self._make_dir()
        self._pull_image()
        client.load(os.path.join(self.img_dir,self.img_name))
        output = client.execute(cmd,
                                bind=bind_dir+":/data",
                                options=['--pwd','/data', '--cleanenv'], stream=True)
        for line in output:
            print(line)

