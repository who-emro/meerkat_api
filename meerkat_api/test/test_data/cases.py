from meerkat_abacus.model import Data
import datetime

public_health_report = [
    # Registers, total cases = 15
    Data(**{'uuid': 'uuid:b59474ed-29e7-490b-a947-558babdf80a5', 'clinic_type': 'Primary', 'district': 4, 'variables': { 'reg_2': 15 }, 'clinic': 8, 'geolocation': '0.2,0.2', 'id': 1, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 11, 32, 51, 80545)}),
    # Cases, total cases = 10, 3 Males, 7 females, 2 per age category, 7 Demo Nationality 3 Null
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9323', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_1": 1, "age_13": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1 }, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 2, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9372', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_1": 1, "age_13": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1, "mod_1":1, "mod_2": 1, "mod_3": 1, "mod_4": 1, "mod_5": 1 }, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 3, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_2": 1, "age_8": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1 }, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 4, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9373', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_2": 1, "age_8": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1 }, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 5, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9374', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_3": 1, "age_9": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1 }, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 6, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9375', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_3": 1, "age_15": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1, "smo_2": 1, "smo_1": 1 }, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 7, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9376', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1 , "age_10": 1, "nat_2": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 8, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9377', 'clinic_type': 'Hospital', 'district': 5, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1 , "age_10": 1, "nat_2": 1, "sta_1": 1, "prc_2": 1, "ncd_2": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 9, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 5, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9378', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_5": 1, "age_11": 1, "nat_2": 1, "sta_1": 1, "prc_2": 1 , "ncd_1": 1, "icb_47": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 10, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9379', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_5": 1, "age_11": 1, "nat_1": 1, "sta_2": 1, "prc_3": 1, "icb_54": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 11, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9312', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1": 1, "gen_2": 1, "prc_1": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 12, 'region': 3, 'country': 1, 'date': datetime.datetime(2016, 4, 30, 23, 54, 16, 49059)})
]


ncd_public_health_report = [
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9377', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_1": 1 , "age_7": 1, "nat_2": 1, "sta_1": 1, "prc_2": 1, "ncd_2": 1, "icb_31": 1 , "mod_4": 1, "mod_5": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 1, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9378', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_1": 1, "age_13": 1, "nat_2": 1, "sta_1": 1, "prc_2": 1 , "ncd_1": 1, "icb_47": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 2, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9377', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1 , "age_10": 1, "nat_2": 1, "sta_1": 1, "prc_2": 1, "ncd_2": 1, "icb_31": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 3, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9378', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_5": 1, "age_11": 1, "nat_2": 1, "sta_1": 1, "prc_2": 1 , "ncd_1": 1, "icb_47": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 4, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9377', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_2": 1 , "age_14": 1, "nat_2": 1, "sta_1": 1, "prc_2": 1, "ncd_2": 1, "icb_31": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 5, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9378', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_2": 1, "age_14": 1, "nat_1": 1, "sta_2": 1, "prc_2": 1 , "ncd_1": 1, "icb_47": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 6 , 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9379', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_5": 1, "age_11": 1, "nat_1": 1, "sta_2": 1, "prc_3": 1, "icb_54": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 11, 'region': 7, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9312', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1": 1 }, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 8, 'region': 3, 'country': 1, 'date': datetime.datetime(2016, 4, 30, 23, 54, 16, 49059)})
]


ncd_report = [
    # Diabetes
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9323', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_1": 1, "age_13": 1, "prc_2": 1, "ncd_1": 1, "lab_4": 1}, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 1, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9372', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_1": 1, "age_13": 1, "prc_2": 1, "ncd_1": 1, "lab_4": 1, "lab_5": 1, "smo_2": 1}, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 2, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_3": 1, "age_8": 1, "prc_2": 1, "ncd_1": 1, "lab_2": 1, "lab_3": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 3, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1, "age_9": 1, "prc_2": 1, "ncd_1": 1, "com_2": 1, "lab_6": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 4, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    #Hypertension
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9323', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_2": 1, "age_14": 1, "prc_2": 1, "ncd_2": 1}, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 5, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9372', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_2": 1, "age_14": 1, "prc_2": 1, "ncd_2": 1, "lab_1": 1, "smo_2": 1, "lab_6":1}, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 6, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_3": 1, "age_8": 1, "prc_2": 1, "ncd_2": 1, "lab_2": 1, "lab_3": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 7, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1, "age_9": 1, "prc_2": 1, "ncd_2": 1, "com_1": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 8, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)})
    
]


pip_report = [
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9323', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_1": 1, "age_7": 1,"nat_1": 1, "sta_1": 1, "pip_1": 1, "pip_2": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 1, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9372', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_1": 1,"nat_1": 1, "sta_1": 1, "age_13": 1, "pip_1": 1, "pip_2": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 2, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_3": 1,"nat_1": 1, "sta_1": 1, "age_9": 1, "pip_1": 1, "pip_2": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 3, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1,"nat_1": 1, "sta_1": 1, "age_10": 1, "pip_1": 1, "pip_2": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 4, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9323', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_2": 1,"nat_1": 1, "sta_1": 1, "age_14": 1, "pip_1": 1, "pip_2": 1, "pip_3": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 5, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 6, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9372', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_2": 1, "nat_1": 1, "sta_1": 1,"age_14": 1, "pip_1": 1, "pip_2": 1, "pip_3": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 6, 'region': 3, 'country': 1, 'date': datetime.datetime(2015, 6, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_3": 1, "nat_1": 1, "sta_1": 1,"age_9": 1, "pip_1": 1, "pip_2": 1}, 'clinic': 10, 'geolocation': '-0.1,0.4', 'id': 7, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 7, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1,"nat_2": 1, "sta_2": 1, "age_10": 1, "pip_1": 1, "pip_2": 1}, 'clinic': 10, 'geolocation': '-0.1,0.4', 'id': 8, 'region': 2, 'country': 1, 'date': datetime.datetime(2015, 7, 30, 23, 54, 16, 49059)}),
        Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1,"nat_2": 1, "sta_2": 1, "age_9": 1, "pip_1": 1, "pip_3": 1}, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 9, 'region': 2, 'country': 1, 'date': datetime.datetime(2016, 4, 30, 23, 54, 16, 49059)})
    
]

refugee_data = [
    # Population and other cumulative numbers should be taken from second entry
    Data(**{'date': datetime.datetime(2015, 1, 1, 0, 0), 'clinic_type': 'Refugee', 'district': 6, 'region': 3, 'clinic': 11, 'variables': {'ref_1': 1, 'ref_2': 1, 'ref_3': 1, 'ref_4': 1, 'ref_5': 1, 'ref_6': 1, 'ref_7': 1, 'ref_8': 1, 'ref_9': 1, 'ref_10': 1, 'ref_11': 1, 'ref_12': 1, 'ref_14': 1, 'ref_13': 50,'ref_15': 1, 'ref_16': 2, 'ref_19': 1, 'ref_20': 1, 'ref_60': 1, 'ref_61': 2, 'ref_95': 1, 'ref_96': 1, 'ref_331': 1, 'ref_332': 1, 'ref_460': 1, 'ref_462': 2, 'ref_557': 1}, 'geolocation': '0,0', 'uuid': 'uuid:fe301f1b-c541-4dde-a355-1552b03e6b7f', 'country': 1, 'id': 1001}),
    Data(**{'date': datetime.datetime(2015, 4, 13, 0, 0), 'clinic_type': 'Refugee', 'district': 6, 'region': 3, 'clinic': 11, 'variables': {'ref_1': 2, 'ref_2': 3, 'ref_3': 4, 'ref_4': 5, 'ref_5': 6, 'ref_6': 7, 'ref_7': 8, 'ref_9': 9, 'ref_10': 10, 'ref_11': 11, 'ref_12': 12, 'ref_14': 5, 'ref_13': 100,'ref_15': 1, 'ref_16': 2,  'ref_19': 1, 'ref_20': 1, 'ref_60': 1, 'ref_61': 2, 'ref_95': 1, 'ref_96': 1, 'ref_331': 1, 'ref_332': 1, 'ref_460': 1, 'ref_462': 2, 'ref_557': 1}, 'geolocation': '0,0', 'uuid': 'uuid:1d337c48-853c-4fc2-93b9-2e5aa74d72b3', 'country': 1, 'id': 1002}),
    Data(**{'date': datetime.datetime(2015, 4, 29, 0, 0), 'clinic_type': 'Refugee', 'district': 5, 'region': 2, 'clinic': 7, 'variables': {'ref_1': 1, 'ref_2': 1, 'ref_3': 1, 'ref_4': 1, 'ref_5': 1, 'ref_6': 1, 'ref_7': 1, 'ref_8': 1, 'ref_9': 1, 'ref_10': 1, 'ref_11': 1, 'ref_12': 1, 'ref_14': 1, 'ref_13': 20, 'ref_15': 1, 'ref_16': 2, 'ref_19': 1, 'ref_20': 1, 'ref_60': 1, 'ref_61': 1, 'ref_95': 1, 'ref_96': 1, 'ref_331': 1, 'ref_332': 1, 'ref_460': 1, 'ref_462': 3, 'ref_557': 1}, 'geolocation': '0,0', 'uuid': 'uuid:c35445a9-eabc-4609-bcb7-4a333c0e23f2', 'country': 1, 'id': 1003}),
    Data(**{'date': datetime.datetime(2016, 4, 29, 0, 0), 'clinic_type': 'Refugee', 'district': 5, 'region': 2, 'clinic': 7, 'variables': {'ref_1': 1, 'ref_2': 1, 'ref_3': 1, 'ref_4': 1, 'ref_5': 1, 'ref_6': 1, 'ref_7': 1, 'ref_8': 1, 'ref_9': 1, 'ref_10': 1, 'ref_11': 1, 'ref_12': 1, 'ref_14': 1}, 'geolocation': '0,0', 'uuid': 'uuid:c35445a9-eabc-4609-bcb7-4a333c0e23f2', 'country': 1, 'id': 1004})
]


year = datetime.datetime.now().year
frontpage = [
    # Registers, total cases = 15
    Data(**{'uuid': 'uuid:b59474ed-29e7-490b-a947-558babdf80a5', 'clinic_type': 'Primary', 'district': 4, 'variables': { 'reg_1': 1, 'reg_2': 15 }, 'clinic': 8, 'geolocation': '0.2,0.2', 'id': 1, 'region': 2, 'country': 1, 'date': datetime.datetime(year, 4, 30, 11, 32, 51, 80545)}),
    # Cases, total cases = 10, 3 Males, 7 females, 2 per age category, 7 Demo Nationality 3 Null
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9323', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_1": 1, "age_13": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1 }, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 2, 'region': 2, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)})
]


map_test = [
    # Cases, total cases = 10, 3 Males, 7 females, 2 per age category, 7 Demo Nationality 3 Null
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9323', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_1": 1, "age_13": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1 }, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 2, 'region': 2, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9372', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_1": 1, "age_13": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1, "mod_1":1, "mod_2": 1, "mod_3": 1, "mod_4": 1, "mod_5": 1 }, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 3, 'region': 2, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9371', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_2": 1, "age_8": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1 }, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 4, 'region': 2, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9373', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_2": 1, "age_8": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1 }, 'clinic': 8, 'geolocation': '-0.1,0.4', 'id': 5, 'region': 2, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9374', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_3": 1, "age_9": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1 }, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 6, 'region': 2, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9375', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_1": 1, "age_3": 1, "age_15": 1, "nat_1": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1, "smo_2": 1, "smo_1": 1 }, 'clinic': 7, 'geolocation': '-0.1,0.4', 'id': 7, 'region': 2, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9376', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1 , "age_10": 1, "nat_2": 1, "sta_1": 1, "prc_1": 1, "cmd_1": 1, "icb_1": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 8, 'region': 3, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9377', 'clinic_type': 'Hospital', 'district': 5, 'variables': {"tot_1":1, "gen_2": 1, "age_4": 1 , "age_10": 1, "nat_2": 1, "sta_1": 1, "prc_2": 1, "ncd_2": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 9, 'region': 3, 'country': 1, 'date': datetime.datetime(year, 5, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9378', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_5": 1, "age_11": 1, "nat_2": 1, "sta_1": 1, "prc_2": 1 , "ncd_1": 1, "icb_47": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 10, 'region': 3, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)}),
    Data(**{'uuid': 'uuid:2d14ec68-c5b3-47d5-90db-eee510ee9379', 'clinic_type': 'Hospital', 'district': 6, 'variables': {"tot_1":1, "gen_2": 1, "age_5": 1, "age_11": 1, "nat_1": 1, "sta_2": 1, "prc_3": 1, "icb_54": 1}, 'clinic': 11, 'geolocation': '-0.1,0.4', 'id': 11, 'region': 3, 'country': 1, 'date': datetime.datetime(year, 4, 30, 23, 54, 16, 49059)}),
]
