from spython.main import Client as client

class SinExecuter(object):
    def __init__(self, name, url, img_dir):
        self.img_name = img_name
        self.img_url = img_url
        self.img_dir = img_dir

    def _make_dir(self):
        subprocess.check_call(['mkdir', '-p', img_dir])

    def _pull_image(self):
        client.pull(image=self.image_url,name=self.image_name, pull_folder=self.image_dir)
        return

    def run(self, cmd, bind_dir):
        self._make_dir()
        self._pull_image()
        client.load(os.path.join(self.image_dir,self.image_name))
        output = client.execute(cmd,
                                bind=','.join(bind_dir+":/data"),
                                options=['--pwd','/data', '--cleanenv'], stream=True)
        with open(log.fname, 'w', buffering=100) as lfile:
            for line in output:
                lfile.write(line)

