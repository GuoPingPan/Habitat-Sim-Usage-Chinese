import glob
import argparse
import os
import shutil
import cv2
from tqdm import tqdm

def img_2_video(args):

    # get imgs path
    img_files = glob.glob(args.dir_path+'/*.png')

    # check dir
    if len(img_files) == 0:
        raise FileExistsError('Empty dir! Please check the path of output imgs.')
    if os.path.exists(args.img_dir):
        raise FileExistsError(f'The img_dir:{args.img_dir} is not empty.')

    # create img dir and move img into dir
    os.mkdir(args.img_dir)
    for img in img_files:
        shutil.move(img,args.img_dir)

    # get imgs'name
    img_files = sorted([img.split('/')[-1] for img in img_files]) 

    # print(img_files)

    # create videowriter
    temp = cv2.imread(os.path.join(args.img_dir,(img_files[0])))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    video = cv2.VideoWriter(args.output, fourcc, fps,(temp.shape[1],temp.shape[0]))

    # show video and write out
    for img_path in tqdm(img_files):
        img = cv2.imread(os.path.join(args.img_dir,img_path))

        video.write(img)

        cv2.imshow("img",img)
        if cv2.waitKey(int(1000/fps)) == ord('q'):
            break
    
    video.release()
    print(f'Finished! The video path is {args.output}')





def main():

    parser = argparse.ArgumentParser(
        description='Arguments for turning habitat output imgs to video.'
    )

    parser.add_argument('dir_path',type=str,default='./',help='the dir path of output imgs')
    parser.add_argument('--img_dir',type=str,default='demo',help='move all imgs into the path')
    parser.add_argument('--output',type=str,default='demo.mp4',help='video output path')

    args = parser.parse_args()

    img_2_video(args)


if __name__=='__main__':
    
    main()

