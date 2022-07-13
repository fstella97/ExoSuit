import numpy as np
import os
import matplotlib.pyplot as plt

def define_csv_save_location(parentDir, expSet):
    print("\n   --------------------")
    print("This run belongs to experiment set:", expSet, "\n")
    path_to_exp_dir =  os.path.join(parentDir, expSet)
    if os.path.isdir(path_to_exp_dir): 
        print("Directory " + expSet + " already exists. New folder is not created.")
    else: 
        os.mkdir(path_to_exp_dir)
        print("New folder with name: " + expSet + " is created.")
    input("Press enter to continue")
    print("\n\n")
    
    return path_to_exp_dir

def rotation_matrix(theta1, theta2, theta3, order='xyz'):
    """
    input
        theta1, theta2, theta3 = rotation angles in rotation order (degrees)
        oreder = rotation order of x,y,z　e.g. XZY rotation -- 'xzy'
    output
        3x3 rotation matrix (numpy array)
    """
    c1 = np.cos(theta1 * np.pi / 180)
    s1 = np.sin(theta1 * np.pi / 180)
    c2 = np.cos(theta2 * np.pi / 180)
    s2 = np.sin(theta2 * np.pi / 180)
    c3 = np.cos(theta3 * np.pi / 180)
    s3 = np.sin(theta3 * np.pi / 180)

    if order == 'xzx':
        matrix=np.array([[c2, -c3*s2, s2*s3],
                         [c1*s2, c1*c2*c3-s1*s3, -c3*s1-c1*c2*s3],
                         [s1*s2, c1*s3+c2*c3*s1, c1*c3-c2*s1*s3]])
    elif order=='xyx':
        matrix=np.array([[c2, s2*s3, c3*s2],
                         [s1*s2, c1*c3-c2*s1*s3, -c1*s3-c2*c3*s1],
                         [-c1*s2, c3*s1+c1*c2*s3, c1*c2*c3-s1*s3]])
    elif order=='yxy':
        matrix=np.array([[c1*c3-c2*s1*s3, s1*s2, c1*s3+c2*c3*s1],
                         [s2*s3, c2, -c3*s2],
                         [-c3*s1-c1*c2*s3, c1*s2, c1*c2*c3-s1*s3]])
    elif order=='yzy':
        matrix=np.array([[c1*c2*c3-s1*s3, -c1*s2, c3*s1+c1*c2*s3],
                         [c3*s2, c2, s2*s3],
                         [-c1*s3-c2*c3*s1, s1*s2, c1*c3-c2*s1*s3]])
    elif order=='zyz':
        matrix=np.array([[c1*c2*c3-s1*s3, -c3*s1-c1*c2*s3, c1*s2],
                         [c1*s3+c2*c3*s1, c1*c3-c2*s1*s3, s1*s2],
                         [-c3*s2, s2*s3, c2]])
    elif order=='zxz':
        matrix=np.array([[c1*c3-c2*s1*s3, -c1*s3-c2*c3*s1, s1*s2],
                         [c3*s1+c1*c2*s3, c1*c2*c3-s1*s3, -c1*s2],
                         [s2*s3, c3*s2, c2]])
    elif order=='xyz':
        matrix=np.array([[c2*c3, -c2*s3, s2],
                         [c1*s3+c3*s1*s2, c1*c3-s1*s2*s3, -c2*s1],
                         [s1*s3-c1*c3*s2, c3*s1+c1*s2*s3, c1*c2]])
    elif order=='xzy':
        matrix=np.array([[c2*c3, -s2, c2*s3],
                         [s1*s3+c1*c3*s2, c1*c2, c1*s2*s3-c3*s1],
                         [c3*s1*s2-c1*s3, c2*s1, c1*c3+s1*s2*s3]])
    elif order=='yxz':
        matrix=np.array([[c1*c3+s1*s2*s3, c3*s1*s2-c1*s3, c2*s1],
                         [c2*s3, c2*c3, -s2],
                         [c1*s2*s3-c3*s1, c1*c3*s2+s1*s3, c1*c2]])
    elif order=='yzx':
        matrix=np.array([[c1*c2, s1*s3-c1*c3*s2, c3*s1+c1*s2*s3],
                         [s2, c2*c3, -c2*s3],
                         [-c2*s1, c1*s3+c3*s1*s2, c1*c3-s1*s2*s3]])
    elif order=='zyx':
        matrix=np.array([[c1*c2, c1*s2*s3-c3*s1, s1*s3+c1*c3*s2],
                         [c2*s1, c1*c3+s1*s2*s3, c3*s1*s2-c1*s3],
                         [-s2, c2*s3, c2*c3]])
    elif order=='zxy':
        matrix=np.array([[c1*c3-s1*s2*s3, -c2*s1, c1*s3+c3*s1*s2],
                         [c3*s1+c1*s2*s3, c1*c2, s1*s3-c1*c3*s2],
                         [-c2*s3, s2, c2*c3]])

    return matrix

def plot_and_save_data(plottingData, xAxisLabel, yAxisLabel, label, savingData, 
                        filename, saveDir, display_plot = True, saveData = True, figsize = (6,8)):

    if display_plot:
        # plot the figures
        f, ax = plt.subplots(len(plottingData) ,1,figsize=figsize)
        
        for i in range(len(plottingData)): 
            
            # plotting
            for j in range(len(plottingData[i]) - 1): 
                ax[i].plot(plottingData[i][0], plottingData[i][j+1], label = label[i][j])

            # x axis label
            if xAxisLabel[i] is not None:
                ax[i].set_xlabel(xAxisLabel[i], fontsize = 15)
        
            # y axis title
            if yAxisLabel[i] is not None:
                ax[i].set_ylabel(yAxisLabel[i], fontsize = 15)

            # legend
            if None not in label[i]:
                ax[i].legend(loc = "best")

        plt.title(filename)
        plt.tight_layout()
        plt.show()

    if saveData:
        save_data = np.transpose(np.vstack(savingData))
        np.savetxt(saveDir + '/' + filename + ".csv", save_data, delimiter = ",")


def y_n_prompt(msg):
    prompt = False
    while 1:
        decision = input(msg)
        if decision == "y" or decision == "Y": 
            prompt = True
            break
        elif decision == "n" or decision == "N":
            break
    return prompt

def obtain_csv_filename(save_dir):
    while 1:
        print("\nEnter csv file name. If you don't care, just press enter")
        filename = input()
        if filename == "": 
            filename += "testing_" + str(int(np.random.random() * 1000000))

        files = os.listdir(save_dir)
        breakLoop = True
        for file in files: 
            if file == filename + ".csv": 
                print("You have a file with the same name. If you continue the prvious file will be overriden.")
                breakLoop = y_n_prompt("Are you SURE you want to continue? (y/n)")
        if breakLoop:
            break
    
    print("This data will correspond with csv with name:", filename + ".csv")

    return filename