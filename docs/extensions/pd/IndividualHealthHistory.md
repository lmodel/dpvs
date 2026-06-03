---
search:
  boost: 10.0
---

# Class: IndividualHealthHistory 


_Information about information health history_



<div data-search-exclude markdown="1">



URI: [pd:IndividualHealthHistory](https://w3id.org/lmodel/dpv/pd/IndividualHealthHistory)





```mermaid
 classDiagram
    class IndividualHealthHistory
    click IndividualHealthHistory href "../IndividualHealthHistory/"
      HealthHistory <|-- IndividualHealthHistory
        click HealthHistory href "../HealthHistory/"
      
      
```





## Inheritance
* [MedicalHealth](MedicalHealth.md) [ [External](External.md)]
    * [HealthHistory](HealthHistory.md)
        * **IndividualHealthHistory**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:IndividualHealthHistory](https://w3id.org/lmodel/dpv/pd/IndividualHealthHistory) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Individual Health History




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#IndividualHealthHistory |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:IndividualHealthHistory |
| native | pd:IndividualHealthHistory |
| exact | dpv_pd:IndividualHealthHistory, dpv_pd_owl:IndividualHealthHistory |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IndividualHealthHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#IndividualHealthHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about information health history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Individual Health History
exact_mappings:
- dpv_pd:IndividualHealthHistory
- dpv_pd_owl:IndividualHealthHistory
is_a: HealthHistory
class_uri: pd:IndividualHealthHistory

```
</details>

### Induced

<details>
```yaml
name: IndividualHealthHistory
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#IndividualHealthHistory
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about information health history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Individual Health History
exact_mappings:
- dpv_pd:IndividualHealthHistory
- dpv_pd_owl:IndividualHealthHistory
is_a: HealthHistory
class_uri: pd:IndividualHealthHistory

```
</details></div>