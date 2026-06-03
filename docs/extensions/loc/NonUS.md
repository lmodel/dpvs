---
search:
  boost: 10.0
---

# Class: NonUS 


_Set of jurisdictions that are not in US_



<div data-search-exclude markdown="1">



URI: [loc:non-US](https://w3id.org/lmodel/dpv/loc/non-US)





```mermaid
 classDiagram
    class NonUS
    click NonUS href "../NonUS/"
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:non-US](https://w3id.org/lmodel/dpv/loc/non-US) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* non-US




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#non-US |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:non-US |
| native | loc:NonUS |
| exact | dpv_loc:non-US, dpv_loc_owl:non-US |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: nonUS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-US
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in US
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-US
exact_mappings:
- dpv_loc:non-US
- dpv_loc_owl:non-US
class_uri: loc:non-US

```
</details>

### Induced

<details>
```yaml
name: nonUS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#non-US
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Set of jurisdictions that are not in US
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- non-US
exact_mappings:
- dpv_loc:non-US
- dpv_loc_owl:non-US
class_uri: loc:non-US

```
</details></div>