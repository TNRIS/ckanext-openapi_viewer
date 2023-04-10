import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class OpenapiViewerPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IConfigurable, inherit=True)
    plugins.implements(plugins.IResourceView, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets', 'ckanext-openapi_viewer')
        
    
    def info(self):
        return {
            'name': 'openapi_viewer',
            'title': 'OpenAPI Viewer',
            'icon': 'file',
            'default_title': 'OpenAPI Viewer'
        }

    def can_view(self, data_dict):
        return data_dict['resource'].get('format', '').lower() == 'json'
    
    def view_template(self, context, data_dict):
        return 'openapi_viewer.html'
