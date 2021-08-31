

import mlrun
from mlrun.platforms import auto_mount, mount_v3io

PROJECT = 'nir-gittest'


def main(local=True):

    mlrun.set_environment(project=PROJECT)

    load_func = mlrun.new_function(name='load',
                                  handler='load_data',
                                  kind='job',
                                  image='mlrun/mlrun',
                                  command='load.py',
                                  source="git://github.com/nirse/remoteproj.git"
                                  )

    load_func.run()

    load_func = mlrun.new_function(name='load1',
                                  handler='load_data1',
                                  kind='job',
                                  image='mlrun/mlrun',
                                  command='folder1/load1.py',
                                  source="git://github.com/nirse/remoteproj.git"
                                  )

    load_func.run()

    train_func = mlrun.new_function(name='train',
                                    handler='train_data',
                                    kind='job',
                                    image='mlrun/mlrun',
                                    command='train.py',
                                    source="git://github.com/nirse/remoteproj.git"
                                   )

    train_func.run()


if __name__ == "__main__":
    main()