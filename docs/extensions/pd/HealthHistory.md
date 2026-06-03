---
search:
  boost: 10.0
---

# Class: HealthHistory 


_Information about health history_



<div data-search-exclude markdown="1">



URI: [pd:HealthHistory](https://w3id.org/lmodel/dpv/pd/HealthHistory)





```mermaid
 classDiagram
    class HealthHistory
    click HealthHistory href "../HealthHistory/"
      MedicalHealth <|-- HealthHistory
        click MedicalHealth href "../MedicalHealth/"
      

      HealthHistory <|-- FamilyHealthHistory
        click FamilyHealthHistory href "../FamilyHealthHistory/"
      HealthHistory <|-- IndividualHealthHistory
        click IndividualHealthHistory href "../IndividualHealthHistory/"
      

      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * **HealthHistory**
        * [FamilyHealthHistory](FamilyHealthHistory.md)
        * [IndividualHealthHistory](IndividualHealthHistory.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:HealthHistory](https://w3id.org/lmodel/dpv/pd/HealthHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Health History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#HealthHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:HealthHistory |
| native | pd:HealthHistory |
| exact | dpv_pd:HealthHistory, dpv_pd_owl:HealthHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HealthHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HealthHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about health history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Health History
exact_mappings:
- dpv_pd:HealthHistory
- dpv_pd_owl:HealthHistory
is_a: MedicalHealth
class_uri: pd:HealthHistory

```
</details>

### Induced

<details>
```yaml
name: HealthHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HealthHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about health history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Health History
exact_mappings:
- dpv_pd:HealthHistory
- dpv_pd_owl:HealthHistory
is_a: MedicalHealth
class_uri: pd:HealthHistory

```
</details></div>