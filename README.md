[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub release](https://img.shields.io/github/release/myTselection/SongBPM.svg)](https://github.com/myTselection/SongBPM/releases)
![GitHub repo size](https://img.shields.io/github/repo-size/myTselection/SongBPM.svg)

[![GitHub issues](https://img.shields.io/github/issues/myTselection/SongBPM.svg)](https://github.com/myTselection/SongBPM/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/myTselection/SongBPM.svg)](https://github.com/myTselection/SongBPM/commits/master)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/myTselection/SongBPM.svg)](https://github.com/myTselection/SongBPM/graphs/commit-activity)

# SongBPM - Home Assistant integration
[SongBPM](https://www.songbpm.com/) Home Assistant custom component integration. SongBPM will try to find the BPM of a song..

This integration is in no way affiliated with SongBPM.

<p align="center"><img src="https://raw.githubusercontent.com/myTselection/SongBPM/master/icon.png"/></p>


## Installation
- [HACS](https://hacs.xyz/): add url https://github.com/myTselection/SongBPM as custom repository (HACS > Integration > option: Custom Repositories)
	- [![Open your Home Assistant instance and open the repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg?style=flat-square)](https://my.home-assistant.io/redirect/hacs_repository/?owner=myTselection&repository=SongBPM&category=integration)

- Restart Home Assistant
- Add 'SongBPM' integration via HA Settings > 'Devices and Services' > 'Integrations'



## Integration

## Status
Still some optimisations are planned, see [Issues](https://github.com/myTselection/SongBPM/issues) section in GitHub.

## Technical pointers
The main logic and API connection related code can be found within source code SongBPM/custom_components/MyEnery:
- [sensor.py](https://github.com/myTselection/SongBPM/blob/master/custom_components/SongBPM/sensor.py)
- [utils.py](https://github.com/myTselection/SongBPM/blob/master/custom_components/SongBPM/utils.py) -> mainly ComponentSession class

All other files just contain boilerplat code for the integration to work wtihin HA or to have some constants/strings/translations.

If you would encounter some issues with this custom component, you can enable extra debug logging by adding below into your `configuration.yaml`:
<details><summary>Click to show example</summary>
	
```
logger:
  default: info
  logs:
     custom_components.songbpm: debug
```
</details>

## Example 