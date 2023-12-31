python image_mixmatch.py \
--gpu_id 0,1,2,3 \
--seed 2022 \
--da uda \
--dset VISDA-C \
--max_epoch 15 \
--lr 5e-3 --s 0 \
--alpha 0.5 \
--output_tar ./experiments/VISDA-C/target/ \
--output ./experiments/VISDA-C/target/mixmatch/ \
--net resnet101 \
--cls_par 0.3 \
--ssl 0.6 \
--choice ent \
--ps 0.0 \
#--savename #YOUR_MODEL_NAME#