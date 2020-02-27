# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class AppServiceCertificateOrderPropertiesAppServiceCertificateNotRenewableReasonsItem(str, Enum):

    registration_status_not_supported_for_renewal = "RegistrationStatusNotSupportedForRenewal"
    expiration_not_in_renewal_time_range = "ExpirationNotInRenewalTimeRange"
    subscription_not_active = "SubscriptionNotActive"

class KeyVaultSecretStatus(str, Enum):
    """Status of the Key Vault secret.
    """

    initialized = "Initialized"
    waiting_on_certificate_order = "WaitingOnCertificateOrder"
    succeeded = "Succeeded"
    certificate_order_failed = "CertificateOrderFailed"
    operation_not_permitted_on_key_vault = "OperationNotPermittedOnKeyVault"
    azure_service_unauthorized_to_access_key_vault = "AzureServiceUnauthorizedToAccessKeyVault"
    key_vault_does_not_exist = "KeyVaultDoesNotExist"
    key_vault_secret_does_not_exist = "KeyVaultSecretDoesNotExist"
    unknown_error = "UnknownError"
    external_private_key = "ExternalPrivateKey"
    unknown = "Unknown"

class CertificateProductType(str, Enum):
    """Certificate product type.
    """

    standard_domain_validated_ssl = "StandardDomainValidatedSsl"
    standard_domain_validated_wild_card_ssl = "StandardDomainValidatedWildCardSsl"

class ProvisioningState(str, Enum):
    """Status of certificate order.
    """

    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    in_progress = "InProgress"
    deleting = "Deleting"

class CertificateOrderStatus(str, Enum):
    """Current order status.
    """

    pendingissuance = "Pendingissuance"
    issued = "Issued"
    revoked = "Revoked"
    canceled = "Canceled"
    denied = "Denied"
    pendingrevocation = "Pendingrevocation"
    pending_rekey = "PendingRekey"
    unused = "Unused"
    expired = "Expired"
    not_submitted = "NotSubmitted"

class AppServiceCertificateOrderPatchResourcePropertiesAppServiceCertificateNotRenewableReasonsItem(str, Enum):

    registration_status_not_supported_for_renewal = "RegistrationStatusNotSupportedForRenewal"
    expiration_not_in_renewal_time_range = "ExpirationNotInRenewalTimeRange"
    subscription_not_active = "SubscriptionNotActive"

class CertificateOrderActionType(str, Enum):
    """Action type.
    """

    certificate_issued = "CertificateIssued"
    certificate_order_canceled = "CertificateOrderCanceled"
    certificate_order_created = "CertificateOrderCreated"
    certificate_revoked = "CertificateRevoked"
    domain_validation_complete = "DomainValidationComplete"
    fraud_detected = "FraudDetected"
    org_name_change = "OrgNameChange"
    org_validation_complete = "OrgValidationComplete"
    san_drop = "SanDrop"
    fraud_cleared = "FraudCleared"
    certificate_expired = "CertificateExpired"
    certificate_expiration_warning = "CertificateExpirationWarning"
    fraud_documentation_required = "FraudDocumentationRequired"
    unknown = "Unknown"

class AzureResourceType(str, Enum):
    """Type of the Azure resource the hostname is assigned to.
    """

    website = "Website"
    traffic_manager = "TrafficManager"

class CustomHostNameDnsRecordType(str, Enum):
    """Type of the DNS record.
    """

    c_name = "CName"
    a = "A"

class HostNameType(str, Enum):
    """Type of the hostname.
    """

    verified = "Verified"
    managed = "Managed"

class DomainPropertiesDomainNotRenewableReasonsItem(str, Enum):

    registration_status_not_supported_for_renewal = "RegistrationStatusNotSupportedForRenewal"
    expiration_not_in_renewal_time_range = "ExpirationNotInRenewalTimeRange"
    subscription_not_active = "SubscriptionNotActive"

class DomainStatus(str, Enum):
    """Domain registration status.
    """

    active = "Active"
    awaiting = "Awaiting"
    cancelled = "Cancelled"
    confiscated = "Confiscated"
    disabled = "Disabled"
    excluded = "Excluded"
    expired = "Expired"
    failed = "Failed"
    held = "Held"
    locked = "Locked"
    parked = "Parked"
    pending = "Pending"
    reserved = "Reserved"
    reverted = "Reverted"
    suspended = "Suspended"
    transferred = "Transferred"
    unknown = "Unknown"
    unlocked = "Unlocked"
    unparked = "Unparked"
    updated = "Updated"
    json_converter_failed = "JsonConverterFailed"

class DnsType(str, Enum):
    """Current DNS type
    """

    azure_dns = "AzureDns"
    default_domain_registrar_dns = "DefaultDomainRegistrarDns"

class DomainPatchResourcePropertiesDomainNotRenewableReasonsItem(str, Enum):

    registration_status_not_supported_for_renewal = "RegistrationStatusNotSupportedForRenewal"
    expiration_not_in_renewal_time_range = "ExpirationNotInRenewalTimeRange"
    subscription_not_active = "SubscriptionNotActive"

class RenderingType(str, Enum):
    """Rendering Type
    """

    no_graph = "NoGraph"
    table = "Table"
    time_series = "TimeSeries"
    time_series_per_instance = "TimeSeriesPerInstance"

class SolutionType(str, Enum):
    """Type of Solution
    """

    quick_solution = "QuickSolution"
    deep_investigation = "DeepInvestigation"
    best_practices = "BestPractices"

class IssueType(str, Enum):
    """Represents the type of the Detector
    """

    service_incident = "ServiceIncident"
    app_deployment = "AppDeployment"
    app_crash = "AppCrash"
    runtime_issue_detected = "RuntimeIssueDetected"
    ase_deployment = "AseDeployment"
    user_issue = "UserIssue"
    platform_issue = "PlatformIssue"
    other = "Other"

class ResourceScopeType(str, Enum):
    """Name of a resource type this recommendation applies, e.g. Subscription, ServerFarm, Site.
    """

    server_farm = "ServerFarm"
    subscription = "Subscription"
    web_site = "WebSite"

class NotificationLevel(str, Enum):
    """Level indicating how critical this recommendation can impact.
    """

    critical = "Critical"
    warning = "Warning"
    information = "Information"
    non_urgent_suggestion = "NonUrgentSuggestion"

class Channels(str, Enum):
    """List of channels that this recommendation can apply.
    """

    notification = "Notification"
    api = "Api"
    email = "Email"
    webhook = "Webhook"
    all = "All"

class ComputeModeOptions(str, Enum):
    """Shared/dedicated workers.
    """

    shared = "Shared"
    dedicated = "Dedicated"
    dynamic = "Dynamic"

class WorkerSizeOptions(str, Enum):
    """Size of the machines.
    """

    small = "Small"
    medium = "Medium"
    large = "Large"
    d1 = "D1"
    d2 = "D2"
    d3 = "D3"
    default = "Default"

class AccessControlEntryAction(str, Enum):
    """Action object.
    """

    permit = "Permit"
    deny = "Deny"

class HostingEnvironmentStatus(str, Enum):
    """Current status of the App Service Environment.
    """

    preparing = "Preparing"
    ready = "Ready"
    scaling = "Scaling"
    deleting = "Deleting"

class InternalLoadBalancingMode(str, Enum):
    """Specifies which endpoints to serve internally in the Virtual Network for the App Service
    Environment.
    """

    none = "None"
    web = "Web"
    publishing = "Publishing"

class AppServicePlanRestrictions(str, Enum):
    """App Service plans this offer is restricted to.
    """

    none = "None"
    free = "Free"
    shared = "Shared"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"

class SslState(str, Enum):
    """SSL type.
    """

    disabled = "Disabled"
    sni_enabled = "SniEnabled"
    ip_based_enabled = "IpBasedEnabled"

class HostType(str, Enum):
    """Indicates whether the hostname is a standard or repository hostname.
    """

    standard = "Standard"
    repository = "Repository"

class ConnectionStringType(str, Enum):
    """Type of database.
    """

    my_sql = "MySql"
    sql_server = "SQLServer"
    sql_azure = "SQLAzure"
    custom = "Custom"
    notification_hub = "NotificationHub"
    service_bus = "ServiceBus"
    event_hub = "EventHub"
    api_hub = "ApiHub"
    doc_db = "DocDb"
    redis_cache = "RedisCache"
    postgre_sql = "PostgreSQL"

class IpFilterTag(str, Enum):
    """Defines what this IP filter will be used for. This is to support IP filtering on proxies.
    """

    default = "Default"
    xff_proxy = "XffProxy"

class ManagedServiceIdentityType(str, Enum):
    """Type of managed service identity.
    """

    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"
    system_assigned_user_assigned = "SystemAssigned, UserAssigned"
    none = "None"

class UsageState(str, Enum):
    """State indicating whether the app has exceeded its quota usage. Read-only.
    """

    normal = "Normal"
    exceeded = "Exceeded"

class SiteAvailabilityState(str, Enum):
    """Management information availability state for the app.
    """

    normal = "Normal"
    limited = "Limited"
    disaster_recovery_mode = "DisasterRecoveryMode"

class AzureStorageType(str, Enum):
    """Type of storage.
    """

    azure_files = "AzureFiles"
    azure_blob = "AzureBlob"

class AzureStorageState(str, Enum):
    """State of the storage account.
    """

    ok = "Ok"
    invalid_credentials = "InvalidCredentials"
    invalid_share = "InvalidShare"

class ScmType(str, Enum):
    """SCM type.
    """

    none = "None"
    dropbox = "Dropbox"
    tfs = "Tfs"
    local_git = "LocalGit"
    git_hub = "GitHub"
    code_plex_git = "CodePlexGit"
    code_plex_hg = "CodePlexHg"
    bitbucket_git = "BitbucketGit"
    bitbucket_hg = "BitbucketHg"
    external_git = "ExternalGit"
    external_hg = "ExternalHg"
    one_drive = "OneDrive"
    vso = "VSO"

class ManagedPipelineMode(str, Enum):
    """Managed pipeline mode.
    """

    integrated = "Integrated"
    classic = "Classic"

class SiteLoadBalancing(str, Enum):
    """Site load balancing.
    """

    weighted_round_robin = "WeightedRoundRobin"
    least_requests = "LeastRequests"
    least_response_time = "LeastResponseTime"
    weighted_total_traffic = "WeightedTotalTraffic"
    request_hash = "RequestHash"

class AutoHealActionType(str, Enum):
    """Predefined action to be taken.
    """

    recycle = "Recycle"
    log_event = "LogEvent"
    custom_action = "CustomAction"

class SupportedTlsVersions(str, Enum):
    """MinTlsVersion: configures the minimum version of TLS required for SSL requests
    """

    one0 = "1.0"
    one1 = "1.1"
    one2 = "1.2"

class FtpsState(str, Enum):
    """State of FTP / FTPS service
    """

    all_allowed = "AllAllowed"
    ftps_only = "FtpsOnly"
    disabled = "Disabled"

class RedundancyMode(str, Enum):
    """Site redundancy mode
    """

    none = "None"
    manual = "Manual"
    failover = "Failover"
    active = "ActiveActive"
    geo_redundant = "GeoRedundant"

class DatabaseType(str, Enum):
    """Database type (e.g. SqlAzure / MySql).
    """

    sql_azure = "SqlAzure"
    my_sql = "MySql"
    local_my_sql = "LocalMySql"
    postgre_sql = "PostgreSql"

class BackupItemStatus(str, Enum):
    """Backup status.
    """

    in_progress = "InProgress"
    failed = "Failed"
    succeeded = "Succeeded"
    timed_out = "TimedOut"
    created = "Created"
    skipped = "Skipped"
    partially_succeeded = "PartiallySucceeded"
    delete_in_progress = "DeleteInProgress"
    delete_failed = "DeleteFailed"
    deleted = "Deleted"

class ContinuousWebJobStatus(str, Enum):
    """Job status.
    """

    initializing = "Initializing"
    starting = "Starting"
    running = "Running"
    pending_restart = "PendingRestart"
    stopped = "Stopped"

class WebJobType(str, Enum):
    """Job type.
    """

    continuous = "Continuous"
    triggered = "Triggered"

class MSDeployLogEntryType(str, Enum):
    """Log entry type
    """

    message = "Message"
    warning = "Warning"
    error = "Error"

class RouteType(str, Enum):
    """The type of route this is:
DEFAULT - By default, every app has routes to the local address
    ranges specified by RFC1918
INHERITED - Routes inherited from the real Virtual Network routes
    STATIC - Static route set on the app only

These values will be used for syncing an app's
    routes with those from a Virtual Network.
    """

    default = "DEFAULT"
    inherited = "INHERITED"
    static = "STATIC"

class PublicCertificateLocation(str, Enum):
    """Public Certificate Location
    """

    current_user_my = "CurrentUserMy"
    local_machine_my = "LocalMachineMy"
    unknown = "Unknown"

class SiteExtensionType(str, Enum):
    """Site extension type.
    """

    gallery = "Gallery"
    web_root = "WebRoot"

class TriggeredWebJobStatus(str, Enum):
    """Job status.
    """

    success = "Success"
    failed = "Failed"
    error = "Error"

class OperationStatus(str, Enum):
    """The current status of the operation.
    """

    in_progress = "InProgress"
    failed = "Failed"
    succeeded = "Succeeded"
    timed_out = "TimedOut"
    created = "Created"

class StatusOptions(str, Enum):
    """App Service plan status.
    """

    ready = "Ready"
    pending = "Pending"
    creating = "Creating"

class Enum4(str, Enum):

    windows = "Windows"
    linux = "Linux"
    windows_functions = "WindowsFunctions"
    linux_functions = "LinuxFunctions"

class Enum5(str, Enum):

    windows = "Windows"
    linux = "Linux"
    windows_functions = "WindowsFunctions"
    linux_functions = "LinuxFunctions"

class CheckNameResourceTypes(str, Enum):
    """Resource type used for verification.
    """

    site = "Site"
    slot = "Slot"
    hosting_environment = "HostingEnvironment"
    publishing_user = "PublishingUser"
    microsoft_web_sites = "Microsoft.Web/sites"
    microsoft_web_sites_slots = "Microsoft.Web/sites/slots"
    microsoft_web_hosting_environments = "Microsoft.Web/hostingEnvironments"
    microsoft_web_publishing_users = "Microsoft.Web/publishingUsers"

class InAvailabilityReasonType(str, Enum):
    """:code:`<code>Invalid</code>` indicates the name provided does not match Azure App Service
    naming requirements. :code:`<code>AlreadyExists</code>` indicates that the name is already in
    use and is therefore unavailable.
    """

    invalid = "Invalid"
    already_exists = "AlreadyExists"

class SkuName(str, Enum):

    free = "Free"
    shared = "Shared"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"
    dynamic = "Dynamic"
    isolated = "Isolated"
    premium_v2 = "PremiumV2"
    elastic_premium = "ElasticPremium"
    elastic_isolated = "ElasticIsolated"

class ValidateResourceTypes(str, Enum):
    """Resource type used for verification.
    """

    server_farm = "ServerFarm"
    site = "Site"

class PublishingProfileFormat(str, Enum):
    """Name of the format. Valid values are: 
FileZilla3
WebDeploy -- default
Ftp
    """

    file_zilla3 = "FileZilla3"
    web_deploy = "WebDeploy"
    ftp = "Ftp"

class DomainType(str, Enum):
    """Valid values are Regular domain: Azure will charge the full price of domain registration,
    SoftDeleted: Purchasing this domain will simply restore it and this operation will not cost
    anything.
    """

    regular = "Regular"
    soft_deleted = "SoftDeleted"

class DnsVerificationTestResult(str, Enum):
    """DNS verification test result.
    """

    passed = "Passed"
    failed = "Failed"
    skipped = "Skipped"

class FrequencyUnit(str, Enum):
    """The unit of time for how often the backup should be executed (e.g. for weekly backup, this
    should be set to Day and FrequencyInterval should be set to 7)
    """

    day = "Day"
    hour = "Hour"

class BackupRestoreOperationType(str, Enum):
    """Operation type.
    """

    default = "Default"
    clone = "Clone"
    relocation = "Relocation"
    snapshot = "Snapshot"
    cloud_fs = "CloudFS"

class UnauthenticatedClientAction(str, Enum):
    """The action to take when an unauthenticated client attempts to access the app.
    """

    redirect_to_login_page = "RedirectToLoginPage"
    allow_anonymous = "AllowAnonymous"

class BuiltInAuthenticationProvider(str, Enum):
    """The default authentication provider to use when multiple providers are configured.
This setting
    is only needed if multiple providers are configured and the unauthenticated client
action is
    set to "RedirectToLoginPage".
    """

    azure_active_directory = "AzureActiveDirectory"
    facebook = "Facebook"
    google = "Google"
    microsoft_account = "MicrosoftAccount"
    twitter = "Twitter"

class LogLevel(str, Enum):
    """Log level.
    """

    off = "Off"
    verbose = "Verbose"
    information = "Information"
    warning = "Warning"
    error = "Error"

class MSDeployProvisioningState(str, Enum):
    """Provisioning state
    """

    accepted = "accepted"
    running = "running"
    succeeded = "succeeded"
    failed = "failed"
    canceled = "canceled"

class CloneAbilityResult(str, Enum):
    """Name of app.
    """

    cloneable = "Cloneable"
    partially_cloneable = "PartiallyCloneable"
    not_cloneable = "NotCloneable"

class MySqlMigrationType(str, Enum):
    """The type of migration operation to be done
    """

    local_to_remote = "LocalToRemote"
    remote_to_local = "RemoteToLocal"
