""" (4.2) Add resource_availability property to a resource

Revision ID: 4dfd8797fdfa
Revises: 3496c876cd1a
Create Date: 2017-09-27 15:57:27.933008

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects import postgresql  # Adding this manually

# revision identifiers, used by Alembic.
revision = '4dfd8797fdfa'
down_revision = '3496c876cd1a'
branch_labels = None
depends_on = None


def upgrade():
    # Adding the enum resource_availability to postgres
    resource_availability = postgresql.ENUM('private', 'tenant', 'global',
                                            name='resource_availability')
    resource_availability.create(op.get_bind())

    # add_column of resource_availability was changed manually
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blueprints', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('blueprints__tenant_id_idx'), 'blueprints', ['_tenant_id'], unique=False)
    op.drop_index('ix_blueprints_created_at', table_name='blueprints')
    op.drop_index('ix_blueprints_id', table_name='blueprints')
    op.add_column('deployment_modifications', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('deployment_modifications__tenant_id_idx'), 'deployment_modifications', ['_tenant_id'], unique=False)
    op.drop_index('ix_deployment_modifications_created_at', table_name='deployment_modifications')
    op.drop_index('ix_deployment_modifications_ended_at', table_name='deployment_modifications')
    op.drop_index('ix_deployment_modifications_id', table_name='deployment_modifications')
    op.add_column('deployment_update_steps', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('deployment_update_steps__tenant_id_idx'), 'deployment_update_steps', ['_tenant_id'], unique=False)
    op.drop_index('ix_deployment_update_steps_id', table_name='deployment_update_steps')
    op.add_column('deployment_updates', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('deployment_updates__tenant_id_idx'), 'deployment_updates', ['_tenant_id'], unique=False)
    op.drop_index('ix_deployment_updates_created_at', table_name='deployment_updates')
    op.drop_index('ix_deployment_updates_id', table_name='deployment_updates')
    op.add_column('deployments', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('deployments__tenant_id_idx'), 'deployments', ['_tenant_id'], unique=False)
    op.drop_index('ix_deployments_created_at', table_name='deployments')
    op.drop_index('ix_deployments_id', table_name='deployments')
    op.add_column('events', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('events__tenant_id_idx'), 'events', ['_tenant_id'], unique=False)
    op.drop_index('ix_events_id', table_name='events')
    op.add_column('executions', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('executions__tenant_id_idx'), 'executions', ['_tenant_id'], unique=False)
    op.drop_index('ix_executions_created_at', table_name='executions')
    op.drop_index('ix_executions_id', table_name='executions')
    op.drop_index('ix_groups_ldap_dn', table_name='groups')
    op.drop_index('ix_groups_name', table_name='groups')
    op.add_column('logs', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('logs__tenant_id_idx'), 'logs', ['_tenant_id'], unique=False)
    op.drop_index('ix_logs_id', table_name='logs')
    op.add_column('node_instances', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('node_instances__tenant_id_idx'), 'node_instances', ['_tenant_id'], unique=False)
    op.drop_index('ix_node_instances_id', table_name='node_instances')
    op.add_column('nodes', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('nodes__tenant_id_idx'), 'nodes', ['_tenant_id'], unique=False)
    op.drop_index('ix_nodes_id', table_name='nodes')
    op.drop_index('ix_nodes_type', table_name='nodes')
    op.add_column('plugins', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('plugins__tenant_id_idx'), 'plugins', ['_tenant_id'], unique=False)
    op.drop_index('ix_plugins_archive_name', table_name='plugins')
    op.drop_index('ix_plugins_id', table_name='plugins')
    op.drop_index('ix_plugins_package_name', table_name='plugins')
    op.drop_index('ix_plugins_uploaded_at', table_name='plugins')
    op.drop_index('ix_roles_name', table_name='roles')
    op.add_column('secrets', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('secrets__tenant_id_idx'), 'secrets', ['_tenant_id'], unique=False)
    op.drop_index('ix_secrets_created_at', table_name='secrets')
    op.drop_index('ix_secrets_id', table_name='secrets')
    op.add_column('snapshots', sa.Column('resource_availability', resource_availability, nullable=True))
    op.create_index(op.f('snapshots__tenant_id_idx'), 'snapshots', ['_tenant_id'], unique=False)
    op.drop_index('ix_snapshots_created_at', table_name='snapshots')
    op.drop_index('ix_snapshots_id', table_name='snapshots')
    op.drop_index('ix_tenants_name', table_name='tenants')
    op.drop_index('ix_users_username', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    op.create_index('ix_tenants_name', 'tenants', ['name'], unique=True)
    op.create_index('ix_snapshots_id', 'snapshots', ['id'], unique=False)
    op.create_index('ix_snapshots_created_at', 'snapshots', ['created_at'], unique=False)
    op.drop_index(op.f('snapshots__tenant_id_idx'), table_name='snapshots')
    op.drop_column('snapshots', 'resource_availability')
    op.create_index('ix_secrets_id', 'secrets', ['id'], unique=False)
    op.create_index('ix_secrets_created_at', 'secrets', ['created_at'], unique=False)
    op.drop_index(op.f('secrets__tenant_id_idx'), table_name='secrets')
    op.drop_column('secrets', 'resource_availability')
    op.create_index('ix_roles_name', 'roles', ['name'], unique=True)
    op.create_index('ix_plugins_uploaded_at', 'plugins', ['uploaded_at'], unique=False)
    op.create_index('ix_plugins_package_name', 'plugins', ['package_name'], unique=False)
    op.create_index('ix_plugins_id', 'plugins', ['id'], unique=False)
    op.create_index('ix_plugins_archive_name', 'plugins', ['archive_name'], unique=False)
    op.drop_index(op.f('plugins__tenant_id_idx'), table_name='plugins')
    op.drop_column('plugins', 'resource_availability')
    op.create_index('ix_nodes_type', 'nodes', ['type'], unique=False)
    op.create_index('ix_nodes_id', 'nodes', ['id'], unique=False)
    op.drop_index(op.f('nodes__tenant_id_idx'), table_name='nodes')
    op.drop_column('nodes', 'resource_availability')
    op.create_index('ix_node_instances_id', 'node_instances', ['id'], unique=False)
    op.drop_index(op.f('node_instances__tenant_id_idx'), table_name='node_instances')
    op.drop_column('node_instances', 'resource_availability')
    op.create_index('ix_logs_id', 'logs', ['id'], unique=False)
    op.drop_index(op.f('logs__tenant_id_idx'), table_name='logs')
    op.drop_column('logs', 'resource_availability')
    op.create_index('ix_groups_name', 'groups', ['name'], unique=True)
    op.create_index('ix_groups_ldap_dn', 'groups', ['ldap_dn'], unique=True)
    op.create_index('ix_executions_id', 'executions', ['id'], unique=False)
    op.create_index('ix_executions_created_at', 'executions', ['created_at'], unique=False)
    op.drop_index(op.f('executions__tenant_id_idx'), table_name='executions')
    op.drop_column('executions', 'resource_availability')
    op.create_index('ix_events_id', 'events', ['id'], unique=False)
    op.drop_index(op.f('events__tenant_id_idx'), table_name='events')
    op.drop_column('events', 'resource_availability')
    op.create_index('ix_deployments_id', 'deployments', ['id'], unique=False)
    op.create_index('ix_deployments_created_at', 'deployments', ['created_at'], unique=False)
    op.drop_index(op.f('deployments__tenant_id_idx'), table_name='deployments')
    op.drop_column('deployments', 'resource_availability')
    op.create_index('ix_deployment_updates_id', 'deployment_updates', ['id'], unique=False)
    op.create_index('ix_deployment_updates_created_at', 'deployment_updates', ['created_at'], unique=False)
    op.drop_index(op.f('deployment_updates__tenant_id_idx'), table_name='deployment_updates')
    op.drop_column('deployment_updates', 'resource_availability')
    op.create_index('ix_deployment_update_steps_id', 'deployment_update_steps', ['id'], unique=False)
    op.drop_index(op.f('deployment_update_steps__tenant_id_idx'), table_name='deployment_update_steps')
    op.drop_column('deployment_update_steps', 'resource_availability')
    op.create_index('ix_deployment_modifications_id', 'deployment_modifications', ['id'], unique=False)
    op.create_index('ix_deployment_modifications_ended_at', 'deployment_modifications', ['ended_at'], unique=False)
    op.create_index('ix_deployment_modifications_created_at', 'deployment_modifications', ['created_at'], unique=False)
    op.drop_index(op.f('deployment_modifications__tenant_id_idx'), table_name='deployment_modifications')
    op.drop_column('deployment_modifications', 'resource_availability')
    op.create_index('ix_blueprints_id', 'blueprints', ['id'], unique=False)
    op.create_index('ix_blueprints_created_at', 'blueprints', ['created_at'], unique=False)
    op.drop_index(op.f('blueprints__tenant_id_idx'), table_name='blueprints')
    op.drop_column('blueprints', 'resource_availability')
    # ### end Alembic commands ###

    # Removing the enum resource_availability from postgres
    resource_availability = postgresql.ENUM('private', 'tenant', 'global',
                                            name='resource_availability')
    resource_availability.drop(op.get_bind())