---
search:
  boost: 10.0
---

# Class: VI 


_Concept representing Country of United States Virgin Islands_



<div data-search-exclude markdown="1">



URI: [loc:VI](https://w3id.org/lmodel/dpv/loc/VI)





```mermaid
 classDiagram
    class VI
    click VI href "../VI/"
      US <|-- VI
        click US href "../US/"
      
      
```





## Inheritance
* [US](US.md)
    * **VI**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:VI](https://w3id.org/lmodel/dpv/loc/VI) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* United States Virgin Islands




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#VI |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:VI |
| native | loc:VI |
| exact | dpv_loc:VI, dpv_loc_owl:VI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: VI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of United States Virgin Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- United States Virgin Islands
exact_mappings:
- dpv_loc:VI
- dpv_loc_owl:VI
is_a: US
class_uri: loc:VI

```
</details>

### Induced

<details>
```yaml
name: VI
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#VI
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of United States Virgin Islands
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- United States Virgin Islands
exact_mappings:
- dpv_loc:VI
- dpv_loc_owl:VI
is_a: US
class_uri: loc:VI

```
</details></div>