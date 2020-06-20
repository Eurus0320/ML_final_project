# ML_final_project
## Running the code


- Run the unet model to train: `python src/models/unet.py train` without saved weights, or with saved weights `python src/models/unet.py train --weights /path/to/weights_file.hdf5`.
- To make a submission (i.e. predictions on testing data): `python src/models/unet.py submit --weights /path/to/weights_file.hdf5 --tiff /path/to/saved_submission.tiff`.

