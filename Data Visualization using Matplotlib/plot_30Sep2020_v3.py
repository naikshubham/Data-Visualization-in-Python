import pandas as pd 
import matplotlib 
import matplotlib.pyplot as plt 
from datetime import datetime
import os
import socket
from matplotlib.dates import DateFormatter
matplotlib.rcParams['figure.figsize'] = [25.0, 12.0]

def load_data(path):
    with open(path, 'r') as f:
        lines = f.read()
    lines = lines.replace('\t\t', ',')
    lines = lines.replace('\t', ',')

    with open('cpu_modified.csv', 'w') as mf:
        mf.write(lines)

def plot_data():
    cpu = pd.read_csv('./cpu_modified.csv')
    cpu = cpu.reset_index()
    cpu = cpu.rename(columns={'index':'Date','Date-Time':'Memory', 'Memory':'Disk','Disk':'CPU'})#.drop('CPU')
    cpu=cpu.dropna(axis=1)
    cpu.Date = pd.to_datetime(cpu.Date.apply(str))
    # cpu = cpu[(cpu.Date >= start_datetime) & (cpu.Date <= end_datetime)]
    cpu = convert_to_integer(cpu)
    fig, ax = plt.subplots()

    ax.plot(cpu["Date"], cpu['Memory'])
    ax.plot(cpu["Date"], cpu['Disk'])
    ax.plot(cpu["Date"], cpu['CPU'])
    ax.legend(['Memory', 'Disk', 'CPU'])
    # Call the show function
    save_path = './'   # path to save graph
    filename = 'plot_'+datetime.now().strftime("%d%b%Y_%H%M%S")  # filename to save
    fig.savefig('{}/{}.jpg'.format(save_path, filename), format='jpg',bbox_inches='tight')

def convert_to_integer(cpu):
    cpu['Memory'] = cpu['Memory'].apply(lambda x:x.replace('%', '').strip())  # replace % with space
    cpu['Disk'] = cpu['Disk'].apply(lambda x:x.replace('%', '').strip())
    cpu['CPU'] = cpu['CPU'].apply(lambda x:x.replace('%', '').strip())
    cpu['Memory'] = pd.to_numeric(cpu['Memory'])  # convert string to numeric values
    cpu['Disk'] = pd.to_numeric(cpu['Disk'])
    cpu['CPU'] = pd.to_numeric(cpu['CPU'])
    return cpu

def get_Host_name_IP(): 
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        # print("Hostname :  ",host_name) 
        # print("IP : ",host_ip) 
    except: 
        host_name = "Unable to get Hostname"
        host_ip = "Unable to get Host IP" 
        # print("Unable to get Hostname and IP") 
    return host_name, host_ip

def plot_subplot():
    cpu = pd.read_csv('./cpu_modified.csv')
    cpu = cpu.reset_index()
    cpu = cpu.rename(columns={'index':'Date','Date-Time':'Memory', 'Memory':'Disk','Disk':'CPU'})#.drop('CPU')
    cpu = cpu.dropna(axis=1)
    cpu.Date = pd.to_datetime(cpu.Date.apply(str))
    cpu = cpu.sort_values('Date').reset_index(drop = True)
    data = cpu
    # data = cpu[(cpu.Date >= start_datetime) & (cpu.Date <= end_datetime)]  # filters date range
    host_name, host_ip = get_Host_name_IP()
    data = convert_to_integer(data) 
    created_date = datetime.now().strftime("%d %b %Y %H:%M:%S")
    date_form = DateFormatter("%d %b %H:%M")

    fig0, ax0 = plt.subplots(3,1)
    fig0.suptitle('Created Date: '+created_date+"\nHost name: "+host_name+"\nHost IP: "+host_ip, fontsize=12)
    ax0[0].plot(data["Date"], data['Memory'], color='green', linewidth=3)
    ax0[0].set_title("Memory Consumption")#\nHost name: "+host_name+"\nHost IP: "+host_ip)
    ax0[0].set_xlabel("Date time")
    ax0[0].set_ylabel("Memory Consumption in %")
    ax0[0].grid()
    ax0[0].xaxis.set_major_formatter(date_form)

    ax0[1].plot(data["Date"], data['Disk'], linewidth=3)
    ax0[1].set_title("Disk IO Consumption") #\nHost name: "+host_name+"\nHost IP: "+host_ip)
    ax0[1].set_xlabel("Date time")
    ax0[1].set_ylabel("Disk IO Consumption in %")
    ax0[1].grid()
    ax0[1].xaxis.set_major_formatter(date_form)
    
    ax0[2].plot(data["Date"], data['CPU'], color='red', linewidth=3)
    ax0[2].set_title("CPU Consumption")#\nHost name: "+host_name+"\nHost IP: "+host_ip)
    ax0[2].set_xlabel("Date time")
    ax0[2].set_ylabel("CPU Consumption in %")
    ax0[2].grid()
    ax0[2].xaxis.set_major_formatter(date_form)

    plt.subplots_adjust(left=0.125,bottom=0.1, right=0.9, top=0.9, wspace=0.2, hspace=0.5)

    fig1, ax1 = plt.subplots()  # memory 
    ax1.text(0.01, 1.05,'Created date:'+created_date, ha='left', va='center', transform=ax1.transAxes)
    ax1.plot(data["Date"], data['Memory'])
    ax1.set_title("Memory Consumption\nHost name: "+host_name+"\nHost IP: "+host_ip)
    ax1.set_xlabel("Date time")
    ax1.set_ylabel("Memory Consumption in %")
    ax1.grid()
    ax1.xaxis.set_major_formatter(date_form)

    fig2, ax2 = plt.subplots()  # disk
    ax2.text(0.01, 1.05,'Created date:'+created_date, ha='left', va='center', transform=ax2.transAxes)
    ax2.plot(data["Date"], data['Disk'], color='C3', linewidth=3)
    ax2.set_title("Disk IO Consumption\nHost name: "+host_name+"\nHost IP: "+host_ip)
    ax2.set_xlabel("Date time")
    ax2.set_ylabel("Disk Consumption in %")
    ax2.xaxis.set_major_formatter(date_form)

    fig3, ax3 = plt.subplots()   # cpu
    ax3.text(0.01, 1.05,'Created date:'+created_date, ha='left', va='center', transform=ax3.transAxes)
    ax3.plot(data["Date"], data['CPU'], color='C4', linewidth=3)
    ax3.set_title("CPU Consumption\nHost name: "+host_name+"\nHost IP: "+host_ip)
    ax3.set_xlabel("Date time")
    ax3.set_ylabel("CPU Consumption in %")
    ax3.xaxis.set_major_formatter(date_form)

    # Call the show function
    save_path = './'   # path to save graph
    filename1 = 'MemoryPlot_'+datetime.now().strftime("%d%b%Y_%H%M%S")  # filename to save
    filename2 = 'DiskPlot_'+datetime.now().strftime("%d%b%Y_%H%M%S")  # filename to save
    filename3 = 'CPUPlot_'+datetime.now().strftime("%d%b%Y_%H%M%S")  # filename to save
    filename0 = 'CombinePlot_'+datetime.now().strftime("%d%b%Y_%H%M%S")

    fig0.savefig('{}/{}.jpg'.format(save_path, filename0), format='jpg',bbox_inches='tight')
    fig1.savefig('{}/{}.jpg'.format(save_path, filename1), format='jpg',bbox_inches='tight')
    fig2.savefig('{}/{}.jpg'.format(save_path, filename2), format='jpg',bbox_inches='tight')
    fig3.savefig('{}/{}.jpg'.format(save_path, filename3), format='jpg',bbox_inches='tight')

if __name__ == '__main__':
    path = './cpu.csv'  # path of csv cpu file
    load_data(path)
    # plot_data()
    plot_subplot()