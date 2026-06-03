---
search:
  boost: 10.0
---

# Class: ProfessionalCertification 


_Information about professional certifications_



<div data-search-exclude markdown="1">



URI: [pd:ProfessionalCertification](https://w3id.org/lmodel/dpv/pd/ProfessionalCertification)





```mermaid
 classDiagram
    class ProfessionalCertification
    click ProfessionalCertification href "../ProfessionalCertification/"
      Professional <|-- ProfessionalCertification
        click Professional href "../Professional/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [Professional](Professional.md)
        * **ProfessionalCertification**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:ProfessionalCertification](https://w3id.org/lmodel/dpv/pd/ProfessionalCertification) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Professional Certification




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#ProfessionalCertification |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:ProfessionalCertification |
| native | pd:ProfessionalCertification |
| exact | dpv_pd:ProfessionalCertification, dpv_pd_owl:ProfessionalCertification |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProfessionalCertification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalCertification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional certifications
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Certification
exact_mappings:
- dpv_pd:ProfessionalCertification
- dpv_pd_owl:ProfessionalCertification
is_a: Professional
class_uri: pd:ProfessionalCertification

```
</details>

### Induced

<details>
```yaml
name: ProfessionalCertification
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ProfessionalCertification
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about professional certifications
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Professional Certification
exact_mappings:
- dpv_pd:ProfessionalCertification
- dpv_pd_owl:ProfessionalCertification
is_a: Professional
class_uri: pd:ProfessionalCertification

```
</details></div>