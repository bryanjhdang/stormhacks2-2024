# Cover Letter Generator
A Python program to generate cover letters. This currently only works with job postings from the SFU co-op board because fields like job title, address, etc., are clearly listed out and can be parsed.

## How to use
1. Clone the project or download it
2. Fill out `coverletter-template.md` with your cover letter text
3. Configure `config.yml` which contains personal information that doesn't change often, like name, email, etc.
4. Copy and paste the job posting information into `posting.txt`. If you don't have access to the SFU coop board, you can manually fill out 
```
python generate.py [options]
```

## Options
- `--pasted` means you copy pasted the job posting into posting.txt. default is false.

## Example
An example is provided in `/example` directory.
