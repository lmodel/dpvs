---
search:
  boost: 10.0
---

# Class: Age 


_Information about age_



<div data-search-exclude markdown="1">



URI: [pd:Age](https://w3id.org/lmodel/dpv/pd/Age)





```mermaid
 classDiagram
    class Age
    click Age href "../Age/"
      PhysicalCharacteristic <|-- Age
        click PhysicalCharacteristic href "../PhysicalCharacteristic/"
      

      Age <|-- AgeRange
        click AgeRange href "../AgeRange/"
      Age <|-- BirthDate
        click BirthDate href "../BirthDate/"
      

      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * **Age**
            * [AgeRange](AgeRange.md)
            * [BirthDate](BirthDate.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Age](https://w3id.org/lmodel/dpv/pd/Age) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Age




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Age |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Age |
| native | pd:Age |
| exact | dpv_pd:Age, dpv_pd_owl:Age |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Age
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Age
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about age
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Age
exact_mappings:
- dpv_pd:Age
- dpv_pd_owl:Age
is_a: PhysicalCharacteristic
class_uri: pd:Age

```
</details>

### Induced

<details>
```yaml
name: Age
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Age
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about age
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Age
exact_mappings:
- dpv_pd:Age
- dpv_pd_owl:Age
is_a: PhysicalCharacteristic
class_uri: pd:Age

```
</details></div>