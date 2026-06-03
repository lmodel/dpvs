---
search:
  boost: 10.0
---

# Class: AS 


_Concept representing Country of American Samoa_



<div data-search-exclude markdown="1">



URI: [loc:AS](https://w3id.org/lmodel/dpv/loc/AS)





```mermaid
 classDiagram
    class AS
    click AS href "../AS/"
      US <|-- AS
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **AS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AS](https://w3id.org/lmodel/dpv/loc/AS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* American Samoa




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AS |
| native | loc:AS |
| exact | dpv_loc:AS, dpv_loc_owl:AS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of American Samoa
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- American Samoa
exact_mappings:
- dpv_loc:AS
- dpv_loc_owl:AS
is_a: US
class_uri: loc:AS

```
</details>

### Induced

<details>
```yaml
name: AS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of American Samoa
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- American Samoa
exact_mappings:
- dpv_loc:AS
- dpv_loc_owl:AS
is_a: US
class_uri: loc:AS

```
</details></div>