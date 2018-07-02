from version_update import VersionUpdater
import human_readable_json






if __name__ == '__main__':

    # find versions that need updating from changelog


    # supply options dictionary
    versionUpdater = VersionUpdater(options)

    versionUpdater.updateVersions()

    human_readable_json.main()



