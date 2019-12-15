from six.moves import urllib
import json
import re

class delScript():
    ''' This script is use to auto delete the asset, dashboard, device, geofence, group, role and token '''

    def __init__(self):
        self.headers = {}
        self.delAssetList = {}
        self.delDashboardList = {}
        self.delDeviceList = {}
        self.delGeofenceList = {}
        self.delGroupList = {}
        self.delRoleList = {}
        self.delTokenList = {}

        self.GroupName1 = "root"
        self.GroupName2 = "QA-testing"
        self.GroupName3 = "QA-testing2"
        
        self.deleteAssetName = "asset2019"          # "asset2019" or "asset-2019"
        self.deleteDeviceName = "device2019"        # "device2019" or "device-2019"
        self.deleteGeofenceName = "geofence2019"
        self.deleteGroupName = "group2019"          # "Group2019" or "group2019" or "group-2019"
        self.deleteRoleName = "role2019"
        self.deleteTokenName = "token2019"

        # exosense-qabot
        self.prodToken = "eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3MDA3OTE3MjczMTAuOTUwNTE5NjExODMwMTkiLCJ0b2tlbiI6InhlMmdmMmMrb3ZuK1dpWE5vUUFhRWZzdzljYitvRmY0ZlN0ZzhYSlByemgzVXhwdFNwZUMyWXlhM2tFdG5iOFBmVHRpRkxTaGlORTRKbXBoWERMZW43bUxSMkNsbWZJUHFoMkYvVENLcDJJYTFEY3RkMFdDVHBCdUxhZzVtcHJpRXhaTk5RcXQ4SEpBQm1udFNCblUzUVV1alBadnhwRWpPeTNOMzBBc1gwT3Nld0l2MFdiNFd3TUZDc0VuRXZaV2VKNWlBMGJ4NXpyU3pjdFZlR2JZVVlWT2xVdVpIN1dRcUViMEwxUEprVVhtL0hzSFdwYVNvZTc4QVpqbkFScUV0akxSMTVYa2l5WnFSQlpZNGJrOXhnWmpGSnNENHJpTWpGMFd4d2NFVFd5MC80UUJzMUpIemk0aFF1aHp3OE40c3lpWmFTRk9PTVNxdW13aGtKWklMNkU9In0="
        self.prodHost = "https://exosense-gql-qabot.hosted.exosite.io/graphql"
        self.prodOrigin = "https://exosense-qabot.apps.exosite.io"
        self.prodContainer = "75ce2640-79d2-431c-95f1-631bde56cbae"

        # murano-exosense
        self.stgToken = "eyJpZCI6ImF1dG9tb24tdG9rZW58MTU3NDA0NjIwMTYwNTAuMjQyMzMwNzY0ODk1NDg2ODgiLCJ0b2tlbiI6ImxHRklFNG5mRG1FWjhpQklRbnhHZDJlcDR0VzFpVVYrUmJUZnkwanhNSnBrMXRWbVo4SWZQR0grU1hGckR1cyttdVowQ0tHaGNTK0JEMk42V2ZrTk5Kc3Z1aFlNM3lXb1VLR0hjQzl2VTVUTi9TZS9iQUFTcHpoUm1SanNWYkkvUWxFVXdOc2wzYjFSc3ZCdlFDTWg0MlVzcjZwMElndWJFSTZKMmFtbThtVjNLSktjWGc0YVZIZysyOFFFRkcxdWQ2VGpSZXQ4RXF1RDhER296VWU5aUJRNkIxdSsreStqbnNiUUZLRGtUWUNVcFJhOGk3UHNvSlBVNWt6UTRXNncwRWROOWFMV3JrSWRwby9yQXJQeVVobHFlV2ZzNmVLVDJEcGdndGpqaWF4cUpBNDFwSXRTQW9Oc2tRVFZjODl2VThFam0yS09kZWZxWXRCc2tPazV5VDA9In0="
        self.stgHost = "https://rcm-graphql.hosted.exosite.io/graphql"
        self.stgOrigin = "https://exosense-stg.apps.exosite-staging.io"
        self.stgContainer = "c25e4621-5e5c-4b2b-8eac-ff78705172f1"      # QA-testing2 = "db5d316a-9585-4356-ae7c-32820e629110"

    def del_script(self, env):
        self.del_asset(env)
        self.del_dashboard(env)
        self.del_device(env)
        self.del_geofence(env)
        self.del_group(env)
        self.del_role(env)
        self.del_toekn(env)

    def del_asset(self, env):
        self.get_asset(env)
        for assetId, assetName in self.delAssetList.items():
            variables = {"id": assetId}
            query = '''
                mutation ($id: ID!) {
                    deleteAsset(id: $id) {
                        id
                    }
                }
            '''
            resp = self.execute(env, query, variables)
            print 'Deleted %s Complete' % assetName

    def del_dashboard(self, env):
        self.get_dashboard(env)
        for dashboardId, dashboardName in self.delDashboardList.items():
            variables = {"id": dashboardId}
            query = '''
                mutation deleteDashboard($id: ID!) {
                    deleteDashboard(id: $id) {
                       id
                    }
                }
            '''
            resp = self.execute(env, query, variables)
            print 'Deleted %s Complete' % dashboardName

    def del_device(self, env):
        self.get_device(env)
        self.get_unclaimed_device(env)
        for deviceId, deviceName in self.delDeviceList.items():
            variables = {"id": deviceId}
            query = '''
                mutation DeleteDevice($id: ID!) {
                    deleteDevice(id: $id) {
                       id
                    }
                }
            '''
            resp = self.execute(env, query, variables)
            print 'Deleted %s Complete' % deviceName

    def del_geofence(self, env):
        self.get_geofence(env)
        for geofenceId, geofenceName in self.delGeofenceList.items():
            variables = {"id": geofenceId}
            query = '''
                mutation deleteGeoFence($id: ID!) {
                    deleteGeoFence(id: $id) {
                        id
                   }
                }
            '''
            resp = self.execute(env, query, variables)
            print 'Deleted %s Complete' % geofenceName

    def del_group(self, env):
        self.get_group(env)
        for groupId, groupName in self.delGroupList.items():
            variables = {"id": groupId}
            query = '''
                mutation ($id: ID!) {
                    deleteGroup(id: $id) {
                        id
                    }
                }
            '''
            resp = self.execute(env, query, variables)
            print 'Deleted %s Complete' % groupName

    def del_role(self, env):
        self.get_role(env)
        for roleId, roleName in self.delRoleList.items():
            variables = {"id": roleId}
            query = '''
                mutation ($id: ID!) {
                    deleteRole(id: $id) {
                        id
                    }
                }
            '''
            resp = self.execute(env, query, variables)
            print 'Deleted %s Complete' % roleName

    def del_toekn(self, env):
        self.get_token(env)
        for tokenId, tokenName in self.delTokenList.items():
            variables = {"id": tokenId}
            query = '''
                mutation deleteUser($id: ID!) {
                    deleteUser(id: $id) {
                        id
                    }
                }
            '''
            resp = self.execute(env, query, variables)
            print 'Deleted %s Complete' % tokenName

    def get_asset(self, env):
        query = '''
            query Assets($pagination: Pagination) @connection(key: "assets") {
                assets(pagination: $pagination) {
                    id
                    name
                    parent {
                        name
                    }
                }
            }
        '''
        assets = self.execute(env, query)
        for asset in assets['data']['assets']:
            if asset['parent']['name'] == self.GroupName1 or asset['parent']['name'] == self.GroupName2 or asset['parent']['name'] == self.GroupName3:
                match = re.search(r"(%s)" % self.deleteAssetName, asset['name'])
                if match:
                    self.delAssetList.update({asset['id']:asset['name']})
        num = len(self.delAssetList)
        if num == 0:
            print 'No asset need to delete'
        else:
            print '--- Start to delete %s assets ---' % num

    def get_dashboard(self, env):
        if env == "1":
            variables = {"id": self.prodContainer}
        if env == "2":
            variables = {"id": self.stgContainer}
        query = '''
            query filteredDashboardContainer($id: ID!){
                dashboardContainer(id: $id) {
                    dashboards {
                        id
                        name
                    }
                }
            }
        '''
        dashboards = self.execute(env, query, variables)
        for dashboard in dashboards['data']['dashboardContainer']['dashboards']:
            match = re.search(r"(%s)" % self.deleteAssetName, dashboard['name'])
            if match:
                self.delDashboardList.update({dashboard['id']:dashboard['name']})
        num = len(self.delDashboardList)
        if num == 0:
            print 'No dashboard need to delete'
        else:
            print '--- Start to delete %s dashboards ---' % num

    def get_device(self, env):
        variables = {"unclaimed": False, "filterObject": {"text": "%s" % self.deleteDeviceName}}
        query = '''
            query GetDevices($unclaimed: Boolean = false, $filterObject: DeviceFilters, $limit: Int = 1000, $offset: Int = 0) @connection(key: "devices") {
                devices(unclaimed: $unclaimed, filters: $filterObject, pagination: { limit: $limit, offset: $offset }) {
                    id
                    identity
                }
            }
        '''
        devices = self.execute(env, query, variables)
        for device in devices['data']['devices']:
            self.delDeviceList.update({device['id']:device['identity']})

    def get_geofence(self, env):
        query = '''
            query Geofences($pagination: Pagination) {
                geoFences(pagination: $pagination) {
                    id
                    name
                }
            }
        '''
        geofences = self.execute(env, query)
        for geofence in geofences['data']['geoFences']:
            match = re.search(r"(%s)" % self.deleteGeofenceName, geofence['name'])
            if match:
                self.delGeofenceList.update({geofence['id']:geofence['name']})
        num = len(self.delGeofenceList)
        if num == 0:
            print 'No geofence need to delete'
        else:
            print '--- Start to delete %s geofences ---' % num

    def get_group(self, env):
        query = '''
            query Groups {
                groups {
                    id
                    name
                }
            }
        '''
        groups = self.execute(env, query)
        for group in groups['data']['groups']:
            match = re.search(r"(%s)" % self.deleteGroupName, group['name'])
            if match:
                self.delGroupList.update({group['id']:group['name']})
        num = len(self.delGroupList)
        if num == 0:
            print 'No group need to delete'
        else:
            print '--- Start to delete %s groups ---' % num

    def get_role(self, env):
        query = '''
            query filteredRoles($filterObject: RoleFilters){
                roles (filters: $filterObject){
                    id
                    name
                }
            }
        '''
        roles = self.execute(env, query)
        for role in roles['data']['roles']:
            match = re.search(r"(%s)" % self.deleteRoleName, role['name'])
            if match:
                self.delRoleList.update({role['id']:role['name']})
        num = len(self.delRoleList)
        if num == 0:
            print 'No role need to delete'
        else:
            print '--- Start to delete %s roles ---' % num

    def get_token(self, env):
        variables = {"filterObject": {"types": ["automation"]}}
        query = '''
            query filteredUsers($filterObject: UserFilters, $pagination: Pagination){
                users(filters: $filterObject, pagination: $pagination) {
                    id
                    name
                }
            }
        '''
        tokens = self.execute(env, query, variables)
        for token in tokens['data']['users']:
            match = re.search(r"(%s)" % self.deleteTokenName, token['name'])
            if match:
                self.delTokenList.update({token['id']:token['name']})
        num = len(self.delTokenList)
        if num == 0:
            print 'No token need to delete'
        else:
            print '--- Start to delete %s tokens ---' % num

    def get_unclaimed_device(self, env):
        variables = {"unclaimed": True, "filterObject": {"text": "%s" % self.deleteDeviceName}}
        query = '''
            query GetDevices($unclaimed: Boolean = false, $filterObject: DeviceFilters, $limit: Int = 1000, $offset: Int = 0) @connection(key: "devices") {
                devices(unclaimed: $unclaimed, filters: $filterObject, pagination: { limit: $limit, offset: $offset }) {
                    id
                    identity
                }
            }
        '''
        devices = self.execute(env, query, variables)
        for device in devices['data']['devices']:
            self.delDeviceList.update({device['id']:device['identity']})
        num = len(self.delDeviceList)
        if num == 0:
            print 'No device need to delete'
        else:
            print '--- Start to delete %s devices ---' % num

    def inject_token(self, env):
        if env == "1":
            self.headers.update({
                'authorization':'Automation %s' % self.prodToken,
                'content-type': 'application/json',
                'origin': self.prodOrigin
            })
        if env == "2":
            self.headers.update({
                'authorization':'Automation %s' % self.stgToken,
                'content-type': 'application/json',
                'origin': self.stgOrigin
            })

    def execute(self, env, query, variables=None):
        self.inject_token(env)
        data = {'query': query, 'variables': variables}
        if env == "1":
            req = urllib.request.Request(self.prodHost, json.dumps(data).encode('utf-8'), self.headers)
        if env == "2":
            req = urllib.request.Request(self.stgHost, json.dumps(data).encode('utf-8'), self.headers)

        try:
            return json.load(urllib.request.urlopen(req))

        except urllib.error.HTTPError as e:
            print((e.read()))
            raise e

data = delScript()
env = raw_input("1: exosense-qabot\n2: exosense-stg\nEnter you want to delete Env.: ")
data.del_script(env)
