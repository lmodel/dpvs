---
search:
  boost: 10.0
---

# Class: Height 


_Information about physical height_



<div data-search-exclude markdown="1">



URI: [pd:Height](https://w3id.org/lmodel/dpv/pd/Height)





```mermaid
 classDiagram
    class Height
    click Height href "../Height/"
      PhysicalCharacteristic <|-- Height
        click PhysicalCharacteristic href "../PhysicalCharacteristic/"
      
      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * **Height**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Height](https://w3id.org/lmodel/dpv/pd/Height) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Height




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Height |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Height |
| native | pd:Height |
| exact | dpv_pd:Height, dpv_pd_owl:Height |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Height
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Height
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about physical height
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Height
exact_mappings:
- dpv_pd:Height
- dpv_pd_owl:Height
is_a: PhysicalCharacteristic
class_uri: pd:Height

```
</details>

### Induced

<details>
```yaml
name: Height
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Height
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about physical height
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Height
exact_mappings:
- dpv_pd:Height
- dpv_pd_owl:Height
is_a: PhysicalCharacteristic
class_uri: pd:Height

```
</details></div>