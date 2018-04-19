-- Exported from QuickDBD: https://www.quickdatatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/schema/DHrY-WRuD0aJNc3K_UzW0g
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE `docente_investigador` (
    `id` int  NOT NULL ,
    `name` string  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `movilidad` (
    `id` int  NOT NULL ,
    `descripcion` string  NOT NULL ,
    `movilidad_nacional_id` int  NOT NULL ,
    `movilidad_internacional_id` int  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `beneficios` (
    `id` int  NOT NULL ,
    `descripcion` string  NOT NULL ,
    `diplomados_id` int  NOT NULL ,
    `movilidad_id` int  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `beneficios_docente` (
    `id` int  NOT NULL ,
    `docente_id` int  NOT NULL ,
    `beneficios_id` int  NOT NULL ,
    `fecha_inicio` date  NOT NULL ,
    `fecha_fin` date  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `generacion_nvo_conocimiento` (
    `id` int  NOT NULL ,
    `type` **  NOT NULL ,
    `producto` file  NOT NULL ,
    `tiempo_entrega` date  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `desarrollo_tecno_innovacion` (
    `id` int  NOT NULL ,
    `types..` **  NOT NULL ,
    `producto` file  NOT NULL ,
    `tiempo_entrega` date  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `apropiacion_conocimiento` (
    `id` int  NOT NULL ,
    `types..` **  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `formacion_rh_cienciatecninno` (
    `id` int  NOT NULL ,
    `types..` **  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `tipologia_productos` (
    `id` int  NOT NULL ,
    `generacion_nvo_cono` int  NOT NULL ,
    `desarrollo_tecn_innovacion` int  NOT NULL ,
    `apropiacion_conocimiento` int  NOT NULL ,
    `formacion_rh_ciencia` int  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

CREATE TABLE `compromisos_docente` (
    `id` int  NOT NULL ,
    `tipologia_productos_id` int  NOT NULL ,
    `beneficios_docentes_id` int  NOT NULL ,
    `descripcion` string  NOT NULL ,
    `fecha_inicio` date  NOT NULL ,
    `fecha_fin` date  NOT NULL ,
    PRIMARY KEY (
        `id`
    )
);

ALTER TABLE `beneficios` ADD CONSTRAINT `fk_beneficios_movilidad_id` FOREIGN KEY(`movilidad_id`)
REFERENCES `movilidad` (`id`);

ALTER TABLE `beneficios_docente` ADD CONSTRAINT `fk_beneficios_docente_docente_id` FOREIGN KEY(`docente_id`)
REFERENCES `docente_investigador` (`id`);

ALTER TABLE `beneficios_docente` ADD CONSTRAINT `fk_beneficios_docente_beneficios_id` FOREIGN KEY(`beneficios_id`)
REFERENCES `beneficios` (`id`);

ALTER TABLE `tipologia_productos` ADD CONSTRAINT `fk_tipologia_productos_generacion_nvo_cono` FOREIGN KEY(`generacion_nvo_cono`)
REFERENCES `generacion_nvo_conocimiento` (`id`);

ALTER TABLE `tipologia_productos` ADD CONSTRAINT `fk_tipologia_productos_desarrollo_tecn_innovacion` FOREIGN KEY(`desarrollo_tecn_innovacion`)
REFERENCES `desarrollo_tecno_innovacion` (`id`);

ALTER TABLE `tipologia_productos` ADD CONSTRAINT `fk_tipologia_productos_apropiacion_conocimiento` FOREIGN KEY(`apropiacion_conocimiento`)
REFERENCES `apropiacion_conocimiento` (`id`);

ALTER TABLE `tipologia_productos` ADD CONSTRAINT `fk_tipologia_productos_formacion_rh_ciencia` FOREIGN KEY(`formacion_rh_ciencia`)
REFERENCES `formacion_rh_cienciatecninno` (`id`);

ALTER TABLE `compromisos_docente` ADD CONSTRAINT `fk_compromisos_docente_tipologia_productos_id` FOREIGN KEY(`tipologia_productos_id`)
REFERENCES `tipologia_productos` (`id`);

ALTER TABLE `compromisos_docente` ADD CONSTRAINT `fk_compromisos_docente_beneficios_docentes_id` FOREIGN KEY(`beneficios_docentes_id`)
REFERENCES `beneficios_docente` (`id`);

