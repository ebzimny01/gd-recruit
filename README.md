# GD Recruit Assistant
This repository includes the code used to build GD Recruit Assistant application.

Visit the [wiki section](https://github.com/ebzimny01/gd-recruit/wiki) for additional information.

## System Requirements
* Microsoft Windows 10 64bit
* Microsoft VC++ 2019 Redistributable (suggested)

## What's New

### Beta v0.4.2 - [Download](https://gdrecruit.s3.amazonaws.com/beta/gdrecruit_beta.exe)
1. Added an Advanced Configuration Option with two config settings you can change within the UI. More info on the wiki can be found [here](https://github.com/ebzimny01/gd-recruit/wiki/BETA-v0.4.2).
   * Always show browser automation (default is enabled) - When enabled, for the actions that require a logged in browser session (e.g. Initialize Recruits and Mark Recruits From Watchlist), you will see the automated actions happening in the Firefox browser that is packaged with the application. This is useful for you to know that it is working and to also respond to the pesky Privacy Notice prompts that have started showing up.
   * Enable debug logging level (default is disable) - When enabled, the application will collect debug level logs typically used for better troubleshooting of issues.
2. Added a Help->About menu option. Selecting this menu option will open your default web browser to the [readme page](https://github.com/ebzimny01/gd-recruit/blob/main/README.md).

### Beta v0.4.1 - [Download](https://gdrecruit.s3.amazonaws.com/beta/gdrecruit_beta.exe?versionId=idokj49OdM0XRgCFNEnmSgzBetU6rbId)
1. Redesigned the authentication experience and implementing cookie reuse. This also means the app will no longer store your username and password. More details [here](https://github.com/ebzimny01/gd-recruit/wiki/New-Auth-Process-in-BETA-v0.4.1) including a quick demo video.
2. Restructured where some of the underlying files are stored:
   * Config directory contains configuration files
   * Seasons directory contains the season database files and will also contain any exported CSV files
   * Cookies directory contains the stored cookies used for quick session reauthentication.
3. Season filenames now include your coachid. This is used for filtering out season files that belong to different coachids. You will only see seasons that match the coachid.

### Beta v0.3.3 - [Download](https://gdrecruit.s3.amazonaws.com/beta/gdrecruit_beta.exe?versionId=08lKdBfSd_dE_jmkoyl90gqIrHE5o_B1)
1. Export to CSV now offers two options -> export All Recruits or export Watchlist Only recruits.
2. The app is free to use. Added button to send PayPal donations for those who wish to do so.

### Beta v0.3.1 - [Download](https://gdrecruit.s3.amazonaws.com/beta/gdrecruit_beta_0_3_1.exe)
[Demo Video](https://youtu.be/Bw7YjvAWvPU)
1. Customize which attributes are highlighted in bold text per position.
2. Customize role ratings calculations for up to 6 different roles per position.
3. Signed recruits will show a gray background. Unsigned recruits will have white background.
4. Recruit Potential now color coded to match GD.
5. Recruits marked from watchlist will show a green check mark icon.
6. Formatted ID and Hometown columns with blue text to give some indication these are clickable links to additional website info.
7. Added ability to export data to .csv file.

Beta v0.2.5 - [Download](https://gdrecruit.s3.amazonaws.com/beta/gdrecruit_beta_0_2_5.exe)

Beta v0.2.3 - [Download](https://gdrecruit.s3.amazonaws.com/beta/gdrecruit_beta.exe?versionId=6kHR4uZ69DNOjNZbgcQ5RqRO9zDFLOUV)

### [Original Prototype Demo Video](https://youtu.be/rj0khucVjzc)
