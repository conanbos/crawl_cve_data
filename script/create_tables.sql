CREATE TABLE NVD_configuration (
    CVE_ID                VARCHAR(64),
    CVE_data_version      VARCHAR(8),
    node_level            INT,
    operator              VARCHAR(8),
    vulnerable            TINYINT(1),
    cpe23Uri              VARCHAR(256),
    cpe_name              VARCHAR(64),
    versionStartIncluding VARCHAR(64),
    versionEndIncluding   VARCHAR(64),
    versionStartExcluding VARCHAR(64),
    versionEndExcluding   VARCHAR(64),
    cpe_version           VARCHAR(64),
    part                  VARCHAR(64),
    vendor                VARCHAR(64),
    product               VARCHAR(64),
    version               VARCHAR(64),
    `update`            VARCHAR(64),
    edition               VARCHAR(64),
    language              VARCHAR(64),
    sw_edition            VARCHAR(64),
    target_sw             VARCHAR(64),
    target_hw             VARCHAR(64),
    other                 TEXT
);



CREATE TABLE nvd_cve (
    data_type              VARCHAR(8),
    data_format            VARCHAR(64),
    data_version           VARCHAR(8),
    CVE_data_meta_ID       VARCHAR(64),
    CVE_data_meta_ASSIGNER VARCHAR(64),
    publishedDate          DATE,
    lastModifiedDate       DATE
);


CREATE TABLE nvd_description (
    CVE_ID VARCHAR(64),
    lang   TEXT,
    value  TEXT
);


CREATE TABLE nvd_impact (
    CVE_ID                     VARCHAR(64),
    V3_version                 VARCHAR(8),
    V3_vectorString            TEXT,
    V3_attackVector            VARCHAR(64),
    V3_attackComplexity        VARCHAR(64),
    V3_privilegesRequired      VARCHAR(64),
    V3_userInteraction         VARCHAR(64),
    V3_scope                   VARCHAR(64),
    V3_confidentialityImpact   VARCHAR(64),
    V3_integrityImpact         VARCHAR(64),
    V3_availabilityImpact      VARCHAR(64),
    V3_baseScore               VARCHAR(64),
    V3_baseSeverity            VARCHAR(64),
    V3_exploitabilityScore     VARCHAR(64),
    V3_impactScore             VARCHAR(64),
    V2_version                 VARCHAR(8),
    V2_vectorString            TEXT,
    V2_accessVector            VARCHAR(64),
    V2_accessComplexity        VARCHAR(64),
    V2_authentication          VARCHAR(64),
    V2_confidentialityImpact   VARCHAR(64),
    V2_integrityImpact         VARCHAR(64),
    V2_availabilityImpact      VARCHAR(64),
    V2_baseScore               VARCHAR(64),
    V2_severity                VARCHAR(64),
    V2_exploitabilityScore     VARCHAR(64),
    V2_impactScore             VARCHAR(64),
    V2_acInsufInfo             TINYINT(1),
    V2_obtainAllPrivilege      TINYINT(1),
    V2_obtainUserPrivilege     TINYINT(1),
    V2_obtainOtherPrivilege    TINYINT(1),
    V2_userInteractionRequired TINYINT(1)
);


CREATE TABLE NVD (
    CVE_data_type         VARCHAR(8),
    CVE_data_format       VARCHAR(8),
    CVE_data_version      VARCHAR(8),
    CVE_data_numberOfCVEs VARCHAR(64),
    CVE_data_timestamp    DATE,
    problemtypeTid        VARCHAR(64),
    referencesTid         VARCHAR(64),
    descriptionTid        VARCHAR(64),
    configurationTid      VARCHAR(64),
    impactTid             VARCHAR(64)
);


CREATE TABLE nvd_problemtype (
    CVE_ID VARCHAR(64),
    lang   VARCHAR(8),
    value  TEXT
);


CREATE TABLE nvd_refs (
    CVE_ID    VARCHAR(64),
    url       TEXT,
    name      TEXT,
    refsource VARCHAR(64),
    tag       VARCHAR(64)
);