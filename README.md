# Compress PDF with iLoveAPI Alfred Workflow
Compresses single PDF via [iLoveAPI](https://www.iloveapi.com/) using [Alfred](https://www.alfredapp.com/)

## Installation
Download [releases/latest](https://github.com/scwxian/pdf_compress_iloveapi/releases/latest/)

## Requirements
- `zsh` (macOS default shell)
- `jq` (download instructions)

## Getting Started
- Create an account in [iLoveAPI](https://www.iloveapi.com/)
- Install Alfred Workflow & ensure `jq` is installed
- Add your `Project Key` during Workflow Configuration

## How it works
Compress PDFs using the [Universal Action](https://www.alfredapp.com/help/features/universal-actions/) or find PDFs with the `ilovepdf` keyword.

The workflow will take your selected PDF, upload, compress, then replace it with the new compressed version with the same name. Currently only works on single PDFs.
