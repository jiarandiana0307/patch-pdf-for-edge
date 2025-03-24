# Patch PDF for Edge

Language: [中文](README.zh_CN.md)

---

Solve the problem of failing to open a PDF in Edge at the last position where you stopped reading.

## Absract

According to [Pick up where you left off on Microsoft Edge PDF Reader][pick-up-where-you-left-off], since release 95 of Edge, there has been a feature added to Edge which let you pick up where you left off on the PDF documents you read in Microsoft Edge. When you reopen your PDF documents in Microsoft Edge, it will start from the position, zoom state and the layout that you were last reading it in.

But somehow, it doesn't work for some PDF documents. This repository will tell you the theory and the workaround for it.

## Theory

Having turned on PDF view setting in Edge, Edge will save the data of the position, zoom state and the layout that you were last reading it in to local storage. When you reopen your PDF documents in Edge, Edge will read and restore the data.

However, the PDF that can't be opened at the last position usually have an `OpenAction` attribute defined in it, and the attribute defines the default actions, e.g. jumping to specific page and executing JavaScript, when you open it.

If a PDF document defines `OpenAction` attribute, the attribute will override the function in Edge that let you pick up where left off on the PDF. For example, if `OpenAction` is defined as jumping to the first page, everytime you open the PDF, you will be navigated to the first page instead of the last page that you read.

So, in order to solve the problem, what we have to do is to modify and remove the `OpenAction` attribute defined in the PDF that failed to be opened at the last position, which is exactly what this repository does.

## Prerequisites

- Python 3

- Edge version >= 95

## Usage

1\. Download this project then enter into the project directory

2\. Install necessary python package

```bash
pip3 install -r requirements.txt
```

3\. Place the PDF that can't be opened at the last position into the project directory

4\. Run the script

```bash
python patch_pdf_for_edge.py
```

Wait for the script to finish executing.

[pick-up-where-you-left-off]: https://techcommunity.microsoft.com/discussions/edgeinsiderannouncements/pick-up-where-you-left-off-on-microsoft-edge-pdf-reader/2771351