---
search:
  boost: 10.0
---

# Class: Weight 


_Information about physical weight_



<div data-search-exclude markdown="1">



URI: [pd:Weight](https://w3id.org/lmodel/dpv/pd/Weight)





```mermaid
 classDiagram
    class Weight
    click Weight href "../Weight/"
      PhysicalCharacteristic <|-- Weight
        click PhysicalCharacteristic href "../PhysicalCharacteristic/"
      
      
```





## Inheritance
* [External](External.md)
    * [PhysicalCharacteristic](PhysicalCharacteristic.md)
        * **Weight**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Weight](https://w3id.org/lmodel/dpv/pd/Weight) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Weight




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Weight |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Weight |
| native | pd:Weight |
| exact | dpv_pd:Weight, dpv_pd_owl:Weight |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Weight
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Weight
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about physical weight
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Weight
exact_mappings:
- dpv_pd:Weight
- dpv_pd_owl:Weight
is_a: PhysicalCharacteristic
class_uri: pd:Weight

```
</details>

### Induced

<details>
```yaml
name: Weight
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Weight
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about physical weight
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Weight
exact_mappings:
- dpv_pd:Weight
- dpv_pd_owl:Weight
is_a: PhysicalCharacteristic
class_uri: pd:Weight

```
</details></div>