# -*- coding: utf-8 -*-
"""
Calibration chessboard PDF generator
"""

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import numpy as np


def mm_to_pt(size):
    return (size / 25.4) * 72.0


def pt_to_mm(size):
    return (size / 72.0) * 25.4


def generate_chessboard(
    paper_size, color, backgroundcolor, no_sq_x, no_sq_y, square_size, date, version
):
    # Generate filename
    filename = (
        "zivid-3d-hand-eye-calibration-checkerboard-"
        + str(no_sq_x)
        + "x"
        + str(no_sq_y)
        + "-"
        + str(square_size)
        + "mm-"
        + str(paper_size)
        + ".pdf"
    )

    if paper_size == "a4":
        width = 297
        height = 210
    if paper_size == "a3":
        width = 420
        height = 297
    if paper_size == "a2":
        width = 594
        height = 420
    if paper_size == "a1":
        width = 841
        height = 594
    if paper_size == "a0":
        width = 1189
        height = 1189

    w_pt = mm_to_pt(width)
    h_pt = mm_to_pt(height)

    board_canvas = canvas.Canvas(filename, pagesize=(w_pt, h_pt), pageCompression=0)

    square_size_pt = mm_to_pt(square_size)

    # Calculate offset to place pattern in the center of the board
    offset_x = (w_pt - no_sq_x * square_size_pt) / 2.0
    offset_y = (h_pt - no_sq_y * square_size_pt) / 2.0

    # Generate chessboard
    board_canvas.setFillColor(backgroundcolor)
    board_canvas.rect(0, 0, mm_to_pt(width), mm_to_pt(height), stroke=0, fill=1)

    board_canvas.setFillColor(color)
    for y in range(no_sq_y):
        for x in range(no_sq_x):
            x0 = offset_x + x * square_size_pt
            y0 = offset_y + y * square_size_pt

            if (y % 2 == 0 and x % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
                board_canvas.rect(
                    x0, y0, square_size_pt, square_size_pt, stroke=0, fill=1
                )

    # Set font and font size
    font_size = 11
    pdfmetrics.registerFont(TTFont("Verdana", "Verdana.ttf"))
    board_canvas.setFont("Verdana", font_size)

    # Generate version text
    version_text = (
        str(no_sq_x)
        + " x "
        + str(no_sq_y)
        + " - "
        + str(square_size)
        + " mm / "
        + version
        + " - "
        + date
    )
    board_canvas.drawString(0.5 * inch, 0.5 * inch, version_text)

    # Generate help text
    help_text = "help.zivid.com"
    text_width = board_canvas.stringWidth(help_text, "Verdana", font_size)
    board_canvas.drawString(w_pt - text_width - 0.5 * inch, 0.5 * inch, help_text)

    board_canvas.showPage()
    board_canvas.save()


#%%

if __name__ == "__main__":

    gray = 0.7
    date = "10/19"
    version = "0.9"

    # A4
    generate_chessboard("a4", (gray, gray, gray), (1, 1, 1), 9, 6, 10, date, version)
    generate_chessboard("a4", (gray, gray, gray), (1, 1, 1), 9, 6, 20, date, version)

    # A3
    generate_chessboard("a3", (gray, gray, gray), (1, 1, 1), 9, 6, 20, date, version)
    generate_chessboard("a3", (gray, gray, gray), (1, 1, 1), 9, 6, 40, date, version)
    # generate_chessboard("a3", (gray, gray, gray), (1, 1, 1), 9, 6, 60, date, versions)

    # A2

    # A1

    # A0
