---
search:
  boost: 10.0
---

# Class: BirthDate 


_Information about birth date_



<div data-search-exclude markdown="1">



URI: [pd:BirthDate](https://w3id.org/lmodel/dpv/pd/BirthDate)





```mermaid
 classDiagram
    class BirthDate
    click BirthDate href "../BirthDate/"
      Age <|-- BirthDate
        click Age href "../Age/"
      
      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * [Age](Age.md)
            * **BirthDate**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:BirthDate](https://w3id.org/lmodel/dpv/pd/BirthDate) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Birth Date




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#BirthDate |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:BirthDate |
| native | pd:BirthDate |
| exact | dpv_pd:BirthDate, dpv_pd_owl:BirthDate |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BirthDate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BirthDate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about birth date
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Birth Date
exact_mappings:
- dpv_pd:BirthDate
- dpv_pd_owl:BirthDate
is_a: Age
class_uri: pd:BirthDate

```
</details>

### Induced

<details>
```yaml
name: BirthDate
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#BirthDate
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about birth date
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Birth Date
exact_mappings:
- dpv_pd:BirthDate
- dpv_pd_owl:BirthDate
is_a: Age
class_uri: pd:BirthDate

```
</details></div>