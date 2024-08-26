# -*- coding: utf-8 -*-
import psycopg2
import os


# establish db connection
def dbConnect():
    _conn = psycopg2.connect(database=, user=, password=, host=, port=)
    _conn.commit()
    return _conn

def handleFile(filePath_, conn_):
    with open(filePath_, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    linesNum = len(lines)
    linesCount = 0
    dataType = ''
    while linesCount < linesNum:
        if lines[linesCount] == '	\n':
            dataType = 'setRtcd'
            linesCount += 1
        elif lines[linesCount] == '	\n':
            dataType = 'setTkgList'
            linesCount += 1
        #elif lines[linesCount] not in ['\n', '\r\n']:
        else:
            if dataType == 'setRtcd':
                linesCount = setRtcdData(lines, linesCount, linesNum, conn_)
            elif dataType == 'setTkgList':
                linesCount = setTkgList(lines, linesCount, conn_)
        #else:
            #linesCount = linesCount + 1
    print("handle file OK")


def setRtcdData(lines_, linesCount_, linesNum ,conn_):
    _rtcdDataDict, _linesCount = handleLinesData(lines_, linesCount_, linesNum)
    D_RTCD = _rtcdDataDict['rtcd']
    D_RTCD_NAME = _rtcdDataDict['rtcdName']
    D_RTCD_TYPE = _rtcdDataDict['rtcdType']
    D_RTCD_HUNT = _rtcdDataDict['rtcdHunt']
    # set TKG_CHN
    D_TKG_CHN = []
    for ch in range(1, 9):
        tkgChnKey = 'tkgId' + str(ch)
        skipVal = 'skipVal' + str(ch)
        if tkgChnKey in _rtcdDataDict:
            tkgChn = chnTransform(_rtcdDataDict[tkgChnKey],_rtcdDataDict[skipVal])
            D_TKG_CHN.append(tkgChn)
        else:
            D_TKG_CHN.append(0)
    # set OVFL_CHN
    D_OVFL_CHN = []
    for ch in range(1, 9):
        ovfChnKey = 'ovftkgId' + str(ch)
        if ovfChnKey in _rtcdDataDict:
            D_OVFL_CHN.append(_rtcdDataDict[ovfChnKey])
        else:
            D_OVFL_CHN.append(0)
    D_RNDM_LNK = _rtcdDataDict['randomLink']

    print(''' INSERT INTO R_RTCD_DATA 
            VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}); '''.format(
                D_RTCD, D_RTCD_NAME, D_RTCD_TYPE, D_RTCD_HUNT, D_TKG_CHN[0], D_TKG_CHN[1], D_TKG_CHN[2],
                D_TKG_CHN[3], D_TKG_CHN[4], D_TKG_CHN[5], D_TKG_CHN[6], D_TKG_CHN[7], D_OVFL_CHN[0], D_OVFL_CHN[1],
                D_OVFL_CHN[2], D_OVFL_CHN[3], D_OVFL_CHN[4], D_OVFL_CHN[5], D_OVFL_CHN[6], D_OVFL_CHN[7], D_RNDM_LNK))
    """
    cur = conn_.cursor()
    try:
        cur.execute(
            ''' INSERT INTO R_RTCD_DATA 
            VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}); '''.format(
                D_RTCD, D_RTCD_NAME, D_RTCD_TYPE, D_RTCD_HUNT, D_TKG_CHN[0], D_TKG_CHN[1], D_TKG_CHN[2],
                D_TKG_CHN[3], D_TKG_CHN[4], D_TKG_CHN[5], D_TKG_CHN[6], D_TKG_CHN[7], D_OVFL_CHN[0], D_OVFL_CHN[1],
                D_OVFL_CHN[2], D_OVFL_CHN[3], D_OVFL_CHN[4], D_OVFL_CHN[5], D_OVFL_CHN[6], D_OVFL_CHN[7], D_RNDM_LNK))
    except Exception as e:
        print('Insert error:', e)
        conn_.rollback()
    else:
        conn_.commit()
    """
    return _linesCount


def handleLinesData(lines_, linesCount_, linesNum_):
    _rtcdDataDict, _linesCount = {}, linesCount_
    while  _linesCount < linesNum_:
        if lines_[_linesCount] in ['\n', '\r\n']:
            break
        line = lines_[_linesCount]
        line = line.replace('\n', '')
        lineSplit = line.split(sep='=')
        _rtcdDataDict[lineSplit[0]] = lineSplit[1]
        _linesCount += 1
    return _rtcdDataDict, _linesCount


def chnTransform(tkgId_,skipVal_):
    _tkgChn = 1
    return _tkgChn


def setTkgList(lines_, linesCount_, conn_):
    _tkgListDict, _linesCount = handleLinesData(lines_,linesCount_)

    D_TKG_ID = _tkgListDict['tkgId']
    D_DEST_N7 = 0
    # D_TKGLINK_ID = _tkgListDict['tkgLinkId']
    D_TKG_NAME = _tkgListDict['tkgName']
    D_NR_OF_TR = _tkgListDict['trNum']
    D_RTE_ID = _tkgListDict['routeId']
    D_NEXT_RTE = _tkgListDict['nextRte']
    D_TKG_STAT = _tkgListDict['tkgState']
    D_TKGP_AV = _tkgListDict['tkgAv']
    D_DIRECTIO = 0
    D_SIG_TYPE = 0
    D_OTH_EXCH = 0
    D_S12_BC = 0
    D_SATELITE = 0
    D_CONTCHK = 0
    D_IDF_PRFX = 0
    D_IDF_POSS = 0
    D_IDF_NB_D = 0
    D_IDF_STRT = 0
    D_ECD_INC = 0
    D_ECD_OUT = 0
    D_PCM_HUNT = _tkgListDict['pcmHunt']
    D_TK_HUNT = _tkgListDict['tkHunt']
    D_FRST_DGTS = 0

    print(''' INSERT INTO R_RTCD_DATA 
            VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}); '''.format(
                D_TKG_ID, D_DEST_N7, D_TKG_NAME, D_NR_OF_TR, D_RTE_ID, D_NEXT_RTE, D_TKG_STAT,
                D_TKGP_AV, D_DIRECTIO, D_SIG_TYPE, D_OTH_EXCH, D_S12_BC, D_SATELITE, D_CONTCHK, D_IDF_PRFX,
                D_IDF_POSS, D_IDF_NB_D, D_IDF_STRT, D_ECD_INC, D_ECD_OUT, D_PCM_HUNT, D_TK_HUNT, D_FRST_DGTS))
    """
    cur = conn_.cursor()
    try:
        cur.execute(
            ''' INSERT INTO R_RTCD_DATA 
            VALUES ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}); '''.format(
                D_TKG_ID, D_DEST_N7, D_TKG_NAME, D_NR_OF_TR, D_RTE_ID, D_NEXT_RTE, D_TKG_STAT,
                D_TKGP_AV, D_DIRECTIO, D_SIG_TYPE, D_OTH_EXCH, D_S12_BC, D_SATELITE, D_CONTCHK, D_IDF_PRFX,
                D_IDF_POSS, D_IDF_NB_D, D_IDF_STRT, D_ECD_INC, D_ECD_OUT, D_PCM_HUNT, D_TK_HUNT, D_FRST_DGTS))
    except Exception as e:
        print('Insert error:', e)
        conn_.rollback()
    else:
        conn_.commit()
    """
    return linesCount_

def main():
    filePath = "data.txt"
    if os.path.exists(filePath):
        fileSize = os.path.getsize(filePath)
        if not fileSize:
            print(filePath, "is empty!")
    else:
        print(filePath, "is not exist")

    # conn = dbConnect()
    conn = 1
    # handle file
    handleFile(filePath, conn)
    # conn.close()

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()
