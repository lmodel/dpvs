---
search:
  boost: 10.0
---

# Class: ProvidedAsCaaS 


_Technology provided as a cloud service consisting of managed compute_

_resources_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsCaaS](https://w3id.org/lmodel/dpv/tech/ProvidedAsCaaS)





```mermaid
 classDiagram
    class ProvidedAsCaaS
    click ProvidedAsCaaS href "../ProvidedAsCaaS/"
      ProvisionMethod <|-- ProvidedAsCaaS
        click ProvisionMethod href "../ProvisionMethod/"
      ProvidedAsCloudService <|-- ProvidedAsCaaS
        click ProvidedAsCloudService href "../ProvidedAsCloudService/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * [ProvidedAsService](ProvidedAsService.md)
        * [ProvidedAsCloudService](ProvidedAsCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * **ProvidedAsCaaS** [ [ProvisionMethod](ProvisionMethod.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsCaaS](https://w3id.org/lmodel/dpv/tech/ProvidedAsCaaS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Compute as a Service (CaaS)Provision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsCaaS |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsCaaS |
| native | tech:ProvidedAsCaaS |
| exact | dpv_tech:ProvidedAsCaaS, dpv_tech_owl:ProvidedAsCaaS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsCaaS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsCaaS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of managed compute

  resources'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Compute as a Service (CaaS)Provision
exact_mappings:
- dpv_tech:ProvidedAsCaaS
- dpv_tech_owl:ProvidedAsCaaS
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsCaaS

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsCaaS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsCaaS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of managed compute

  resources'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Compute as a Service (CaaS)Provision
exact_mappings:
- dpv_tech:ProvidedAsCaaS
- dpv_tech_owl:ProvidedAsCaaS
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsCaaS

```
</details></div>