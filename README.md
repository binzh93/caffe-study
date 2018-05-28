# caffe-study

## Before training, watching the GPU use status：nvidia-smi
## If some PID in use,use the following instructions：kill -9 PID
## While you are in training, use the following to Check the memory use of your GPU：watch -n 10 nvidia-smi












## finetune
step1：open terminal
step2：cd caffe
step3：./build/tools/caffe train --solver ·solver_path] --weights [model_path] --gpu all

such as:
./build/tools/caffe train --solver /data/pycaffe-file/proto_file/solver.prototxt --weights /data/pycaffe-file/ResNet-50-model.caffemodel --gpu all



./build/tools/compute_image_mean examples/mnist/mnist_train_lmdb examples/mnist/mean.binaryproto

