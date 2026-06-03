---
search:
  boost: 10.0
---

# Class: HealthRecord 


_Information about health record_



<div data-search-exclude markdown="1">



URI: [pd:HealthRecord](https://w3id.org/lmodel/dpv/pd/HealthRecord)





```mermaid
 classDiagram
    class HealthRecord
    click HealthRecord href "../HealthRecord/"
      MedicalHealth <|-- HealthRecord
        click MedicalHealth href "../MedicalHealth/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * **HealthRecord**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:HealthRecord](https://w3id.org/lmodel/dpv/pd/HealthRecord) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Health Record




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#HealthRecord |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:HealthRecord |
| native | pd:HealthRecord |
| exact | dpv_pd:HealthRecord, dpv_pd_owl:HealthRecord |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HealthRecord
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HealthRecord
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about health record
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Health Record
exact_mappings:
- dpv_pd:HealthRecord
- dpv_pd_owl:HealthRecord
is_a: MedicalHealth
class_uri: pd:HealthRecord

```
</details>

### Induced

<details>
```yaml
name: HealthRecord
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HealthRecord
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about health record
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Health Record
exact_mappings:
- dpv_pd:HealthRecord
- dpv_pd_owl:HealthRecord
is_a: MedicalHealth
class_uri: pd:HealthRecord

```
</details></div>