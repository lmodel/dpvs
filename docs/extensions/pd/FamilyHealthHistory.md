---
search:
  boost: 10.0
---

# Class: FamilyHealthHistory 


_Information about family health history_



<div data-search-exclude markdown="1">



URI: [pd:FamilyHealthHistory](https://w3id.org/lmodel/dpv/pd/FamilyHealthHistory)





```mermaid
 classDiagram
    class FamilyHealthHistory
    click FamilyHealthHistory href "../FamilyHealthHistory/"
      HealthHistory <|-- FamilyHealthHistory
        click HealthHistory href "../HealthHistory/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * [HealthHistory](HealthHistory.md)
        * **FamilyHealthHistory**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FamilyHealthHistory](https://w3id.org/lmodel/dpv/pd/FamilyHealthHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Family Health History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FamilyHealthHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FamilyHealthHistory |
| native | pd:FamilyHealthHistory |
| exact | dpv_pd:FamilyHealthHistory, dpv_pd_owl:FamilyHealthHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FamilyHealthHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FamilyHealthHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about family health history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Family Health History
exact_mappings:
- dpv_pd:FamilyHealthHistory
- dpv_pd_owl:FamilyHealthHistory
is_a: HealthHistory
class_uri: pd:FamilyHealthHistory

```
</details>

### Induced

<details>
```yaml
name: FamilyHealthHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FamilyHealthHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about family health history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Family Health History
exact_mappings:
- dpv_pd:FamilyHealthHistory
- dpv_pd_owl:FamilyHealthHistory
is_a: HealthHistory
class_uri: pd:FamilyHealthHistory

```
</details></div>