---
search:
  boost: 10.0
---

# Class: Gender 


_Information about gender_



<div data-search-exclude markdown="1">



URI: [pd:Gender](https://w3id.org/lmodel/dpv/pd/Gender)





```mermaid
 classDiagram
    class Gender
    click Gender href "../Gender/"
      PhysicalCharacteristic <|-- Gender
        click PhysicalCharacteristic href "../PhysicalCharacteristic/"
      
      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * **Gender**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Gender](https://w3id.org/lmodel/dpv/pd/Gender) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Gender




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Gender |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Gender |
| native | pd:Gender |
| exact | dpv_pd:Gender, dpv_pd_owl:Gender |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gender
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Gender
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about gender
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Gender
exact_mappings:
- dpv_pd:Gender
- dpv_pd_owl:Gender
is_a: PhysicalCharacteristic
class_uri: pd:Gender

```
</details>

### Induced

<details>
```yaml
name: Gender
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Gender
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about gender
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Gender
exact_mappings:
- dpv_pd:Gender
- dpv_pd_owl:Gender
is_a: PhysicalCharacteristic
class_uri: pd:Gender

```
</details></div>